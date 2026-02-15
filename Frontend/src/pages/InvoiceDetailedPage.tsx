import
{
    Button,
    Card,
    CardBody,
    Divider,
    Spinner,
    Table,
    TableBody,
    TableCell,
    TableColumn,
    TableHeader,
    TableRow,
} from "@heroui/react";
import axios from "axios";
import { useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router";
import type { InvoiceItem, InvoiceWithItems } from "../interfaces/InvoiceI";
import { ENDPOINT } from "../config/app.config";



export default function InvoiceDetailedPage()
{


    const { id } = useParams();
    const [invoice, setInvoice] = useState<InvoiceWithItems | null>(null);
    const [loading, setLoading] = useState(true);
    const [notFound, setNotFound] = useState(false);

    const navigate = useNavigate();

    const fetchInvoice = async () =>
    {
        try
        {
            const res = await axios.get(
                ENDPOINT + `invoices/${id}`
            );
            setInvoice(res.data.invoice);
        }
        catch
        {
            setNotFound(true);
        } finally
        {
            setLoading(false);
        }
    };

    const groupedItems = useMemo(() =>
    {
        if (!invoice) return {};

        return invoice.invoice_items.reduce<Record<string, InvoiceItem[]>>(
            (acc, item) =>
            {
                const category = item.service.category;
                if (!acc[category])
                {
                    acc[category] = [];
                }
                acc[category].push(item);
                return acc;
            },
            {}
        );
    }, [invoice]);




    useEffect(() =>
    {
        fetchInvoice();
    }, [id]);


    useEffect(() =>
    {
        if (notFound)
        {
            navigate("/404", { replace: true });
        }
    }, [notFound, navigate]);

    if (loading)
    {
        return (
            <div className="flex justify-center py-20">
                <Spinner label="Loading invoice..." />
            </div>
        );
    }

    if (!invoice)
    {
        return null;
    }

    return (
        <div className="max-w-5xl mx-auto p-6 print:p-0">
            {/* Header */}
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">Invoice</h1>
                <Button color="primary" onPress={() => window.print()}>
                    Print Invoice
                </Button>
            </div>

            <Card>
                <CardBody className="space-y-6">
                    {/* Invoice Meta */}
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <p><strong>Invoice No:</strong> {invoice.invoice_no}</p>
                            <p><strong>Date:</strong> {invoice.invoice_date}</p>
                            <p><strong>Reception Engineer:</strong> {invoice.reception_engineer}</p>
                        </div>
                        <div>
                            <p><strong>Customer:</strong> {invoice.customer.name}</p>
                            <p><strong>Email:</strong> {invoice.customer.email}</p>
                            <p><strong>Phone:</strong> {invoice.customer.phone}</p>
                        </div>
                    </div>

                    <Divider />

                    {/* Car Info */}
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <p><strong>Car Model:</strong> {invoice.car.model_name}</p>
                            <p><strong>Plate No:</strong> {invoice.car.plate_no}</p>
                        </div>
                        <div>
                            <p><strong>Chassis No:</strong> {invoice.car.chassis_no}</p>
                            <p><strong>Motor No:</strong> {invoice.car.motor_no}</p>
                        </div>
                    </div>

                    <Divider />

                    {/* Items Table */}
                    {Object.entries(groupedItems).map(([category, items]) => (
                        <div key={category} className="space-y-3">
                            <h2 className="text-lg font-semibold capitalize">
                                {category.replace("_", " ")}
                            </h2>

                            <Table aria-label={`${category} services`}>
                                <TableHeader>
                                    <TableColumn>#</TableColumn>
                                    <TableColumn>Service</TableColumn>
                                    <TableColumn>Code</TableColumn>
                                    <TableColumn>Qty</TableColumn>
                                    <TableColumn>Unit Price</TableColumn>
                                    <TableColumn>Discount</TableColumn>
                                    <TableColumn>Total</TableColumn>
                                </TableHeader>

                                <TableBody>
                                    {items.map((item, index) => (
                                        <TableRow key={item.id}>
                                            <TableCell>{index + 1}</TableCell>
                                            <TableCell>{item.service.name}</TableCell>
                                            <TableCell>{item.service.service_code}</TableCell>
                                            <TableCell>{item.quantity}</TableCell>
                                            <TableCell>{item.price.toFixed(2)}</TableCell>
                                            <TableCell>{item.discount.toFixed(2)}</TableCell>
                                            <TableCell>{item.total_price.toFixed(2)}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </div>
                    ))}


                    <Divider />

                    {/* Total */}
                    <div className="flex justify-end">
                        <div className="text-right">
                            <p className="text-lg font-semibold">
                                Total Amount
                            </p>
                            <p className="text-2xl font-bold">
                                {invoice.total_amount.toFixed(2)}
                            </p>
                        </div>
                    </div>
                </CardBody>
            </Card>
        </div>
    );
}
