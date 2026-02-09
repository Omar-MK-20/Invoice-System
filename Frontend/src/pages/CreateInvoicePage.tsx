import
{
    addToast,
    Button,
    Card,
    CardBody,
    Input,
    Select,
    SelectItem,
} from "@heroui/react";
import { zodResolver } from "@hookform/resolvers/zod";
import axios, { AxiosError } from "axios";
import { useEffect, useState } from "react";
import
{
    Controller,
    useFieldArray,
    useForm,
    useWatch,
} from "react-hook-form";

import
{
    createInvoiceSchema,
    type CreateInvoiceForm,
} from "../schemas/invoiceSchema";

/* =======================
   Types
======================= */

type Customer = {
    id: number;
    name: string;
};

type Car = {
    id: number;
    model_name: string;
    plate_no: string;
};

type Service = {
    id: number;
    name: string;
    price: number;
};

/* =======================
   Component
======================= */

export default function CreateInvoicePage()
{
    const [customers, setCustomers] = useState<Customer[]>([]);
    const [cars, setCars] = useState<Car[]>([]);
    const [services, setServices] = useState<Service[]>([]);

    const {
        control,
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<CreateInvoiceForm>({
        resolver: zodResolver(createInvoiceSchema),
        defaultValues: {
            invoice_items: [
                {
                    service_id: 0,
                    quantity: 1,
                    discount: 0,
                },
            ],
        },
    });

    const { fields, append, remove } = useFieldArray({
        control,
        name: "invoice_items",
    });

    /* =======================
       Watch selected customer
    ======================= */

    const selectedCustomerName = useWatch({
        control,
        name: "customer_name",
    });

    /* =======================
       Load initial data
    ======================= */

    useEffect(() =>
    {
        async function loadInitialData()
        {
            const [customersRes, servicesRes] = await Promise.all([
                axios.get("http://localhost:8000/customers"),
                axios.get("http://localhost:8000/services"),
            ]);

            setCustomers(customersRes.data.customers);
            setServices(servicesRes.data.services);
        }

        loadInitialData();
    }, []);

    /* =======================
       Load cars when customer changes
    ======================= */

    useEffect(() =>
    {
        async function loadCars()
        {
            if (!selectedCustomerName)
            {
                setCars([]);
                return;
            }

            const customersRes = await axios.get(
                "http://localhost:8000/customers"
            );

            const customer = customersRes.data.customers.find(
                (c: Customer) => c.name === selectedCustomerName
            );

            if (!customer) return;

            const customerRes = await axios.get(
                `http://localhost:8000/customers/${customer.id}`
            );

            setCars(customerRes.data.customer.cars);
        }

        loadCars();
    }, [selectedCustomerName]);

    /* =======================
       Submit
    ======================= */

    async function onSubmit(data: CreateInvoiceForm)
    {
        console.log("SUBMIT ✅", data);
        try
        {
            const res = await axios.post("http://localhost:8000/invoices", data);
            addToast({
                title: res?.data?.message,
                color: "success",
            });
        }
        catch (error)
        {
            let message = "Something went wrong while fetching invoices";

            if (error instanceof AxiosError)
            {
                message = error?.response?.data?.detail?.error ?? message;
            }

            addToast({
                title: "No Results",
                description: message,
                color: "danger",
            });
        }
    }

    /* =======================
       Render
    ======================= */

    return (
        <div className="max-w-5xl mx-auto p-6 space-y-6">
            <h1 className="text-2xl font-bold">Create Invoice</h1>

            <form
                onSubmit={handleSubmit(onSubmit, (e) =>
                    console.log("FORM ERRORS ❌", e)
                )}
                className="space-y-6"
            >
                {/* ================= Invoice Info ================= */}
                <Card>
                    <CardBody className="grid grid-cols-2 gap-4">
                        <Input
                            label="Invoice No"
                            {...register("invoice_no")}
                            isInvalid={!!errors.invoice_no}
                            errorMessage={errors.invoice_no?.message}
                        />

                        <Input
                            type="date"
                            label="Invoice Date"
                            {...register("invoice_date")}
                        />

                        {/* Customer */}
                        <Controller
                            name="customer_name"
                            control={control}
                            render={({ field }) => (
                                <Select
                                    label="Customer"
                                    selectedKeys={
                                        field.value ? new Set([field.value]) : new Set()
                                    }
                                    onSelectionChange={(keys) =>
                                    {
                                        const value = [...keys][0];
                                        field.onChange(value ?? "");
                                    }}
                                    isInvalid={!!errors.customer_name}
                                    errorMessage={errors.customer_name?.message}
                                >
                                    {customers.map((customer) => (
                                        <SelectItem
                                            key={customer.name}
                                            textValue={customer.name}
                                        >
                                            {customer.name}
                                        </SelectItem>
                                    ))}
                                </Select>
                            )}
                        />

                        {/* Car */}
                        <Controller
                            name="car_id"
                            control={control}
                            render={({ field }) => (
                                <Select
                                    label="Car"
                                    isDisabled={!cars.length}
                                    selectedKeys={
                                        field.value
                                            ? new Set([String(field.value)])
                                            : new Set()
                                    }
                                    onSelectionChange={(keys) =>
                                    {
                                        const value = [...keys][0];
                                        field.onChange(value ? Number(value) : undefined);
                                    }}
                                    isInvalid={!!errors.car_id}
                                    errorMessage={errors.car_id?.message}
                                >
                                    {cars.map((car) => (
                                        <SelectItem key={String(car.id)}>
                                            {car.model_name} — {car.plate_no}
                                        </SelectItem>
                                    ))}
                                </Select>
                            )}
                        />
                    </CardBody>
                </Card>

                {/* ================= Invoice Items ================= */}
                <Card>
                    <CardBody className="space-y-4">
                        <h2 className="text-lg font-semibold">Invoice Items</h2>

                        {fields.map((field, index) => (
                            <div
                                key={field.id}
                                className="grid grid-cols-4 gap-3 items-end"
                            >
                                <Controller
                                    name={`invoice_items.${index}.service_id`}
                                    control={control}
                                    render={({ field }) => (
                                        <Select
                                            label="Service"
                                            selectedKeys={
                                                field.value !== null
                                                    ? new Set([String(field.value)])
                                                    : new Set()
                                            }
                                            onSelectionChange={(keys) =>
                                            {
                                                const value = [...keys][0];
                                                field.onChange(
                                                    value ? Number(value) : null
                                                );
                                            }}
                                        >
                                            {services.map((service) => (
                                                <SelectItem
                                                    key={String(service.id)}
                                                    textValue={service.name}
                                                >
                                                    {service.name}
                                                </SelectItem>
                                            ))}
                                        </Select>
                                    )}
                                />

                                <Input
                                    type="number"
                                    label="Quantity"
                                    {...register(
                                        `invoice_items.${index}.quantity`,
                                        { valueAsNumber: true }
                                    )}
                                />

                                <Input
                                    type="number"
                                    label="Discount"
                                    {...register(
                                        `invoice_items.${index}.discount`,
                                        { valueAsNumber: true }
                                    )}
                                />

                                <Button
                                    color="danger"
                                    variant="flat"
                                    onPress={() => remove(index)}
                                >
                                    Remove
                                </Button>
                            </div>
                        ))}

                        <Button
                            color="secondary"
                            variant="flat"
                            onPress={() =>
                                append({
                                    service_id: 0,
                                    quantity: 1,
                                    discount: 0,
                                })
                            }
                        >
                            + Add Item
                        </Button>
                    </CardBody>
                </Card>

                {/* ================= Submit ================= */}
                <div className="flex justify-end">
                    <Button color="primary" type="submit">
                        Create Invoice
                    </Button>
                </div>
            </form>
        </div>
    );
}
