import
{
    addToast,
    Button,
    Input,
    Spinner,
    Table,
    TableBody,
    TableCell,
    TableColumn,
    TableHeader,
    TableRow,
} from "@heroui/react";
import { useAsyncList } from "@react-stately/data";
import axios, { AxiosError, type AxiosResponse } from "axios";
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { type Invoice, type InvoicesResponse } from "../interfaces/InvoiceI";

export default function InvoicesList()
{

    const [filters, setFilters] = useState({
        invoiceNo: "",
        customerName: "",
        dateFrom: "",
        dateTo: "",
    });




    const navigate = useNavigate();
    const [isLoading, setIsLoading] = React.useState(true);

    const list = useAsyncList<Invoice>({
        async load({ signal })
        {
            setIsLoading(true);

            try
            {
                const res: AxiosResponse<InvoicesResponse> = await axios.get(
                    "http://localhost:8000/invoices",
                    {
                        signal,
                        params: {
                            invoiceNo: filters.invoiceNo || undefined,
                            customerName: filters.customerName || undefined,
                            dateFrom: filters.dateFrom || undefined,
                            dateTo: filters.dateTo || undefined,
                        },
                    }
                );

                return { items: res.data.invoices };
            }
            catch (error)
            {
                // Axios error with backend response
                if (axios.isCancel(error))
                {
                    return { items: [] };
                }

                let message = "Something went wrong while fetching invoices";

                if (error instanceof AxiosError)
                {
                    message = error?.response?.data?.detail?.error ?? message;
                }

                addToast({
                    title: "No Results",
                    description: message,
                    color: "warning",
                });

                return { items: [] };
            } finally
            {
                setIsLoading(false);
            }
        }
        ,

        async sort({ items, sortDescriptor })
        {
            return {
                items: [...items].sort((a, b) =>
                {
                    let first;
                    let second;

                    switch (sortDescriptor.column)
                    {
                        case "customer":
                            first = a.customer.name;
                            second = b.customer.name;
                            break;
                        case "car":
                            first = a.car.model_name;
                            second = b.car.model_name;
                            break;
                        default:
                            first = a[sortDescriptor.column as keyof Invoice];
                            second = b[sortDescriptor.column as keyof Invoice];
                    }

                    let cmp =
                        (typeof first === "number" ? first : String(first)) <
                            (typeof second === "number" ? second : String(second))
                            ? -1
                            : 1;

                    if (sortDescriptor.direction === "descending")
                    {
                        cmp *= -1;
                    }

                    return cmp;
                }),
            };
        },
    });


    useEffect(() =>
    {
        list.reload();
    }, [filters]);

    return (
        <div className="px-6 py-8">
            <h1 className="text-2xl font-bold mb-6">Invoices</h1>


            <div className="flex flex-wrap gap-4 mb-6 items-end">
                <Input
                    label="Invoice No"
                    placeholder="INV-2023-001"
                    value={filters.invoiceNo}
                    onValueChange={(value) =>
                        setFilters({ ...filters, invoiceNo: value })
                    }
                    className="max-w-xs"
                />

                <Input
                    label="Customer Name"
                    placeholder="Omar Ibrahim"
                    value={filters.customerName}
                    onValueChange={(value) =>
                        setFilters({ ...filters, customerName: value })
                    }
                    className="max-w-xs"
                />

                <Input
                    type="date"
                    label="From"
                    value={filters.dateFrom}
                    onValueChange={(value) =>
                        setFilters({ ...filters, dateFrom: value })
                    }
                    className="max-w-xs"
                />

                <Input
                    type="date"
                    label="To"
                    value={filters.dateTo}
                    onValueChange={(value) =>
                        setFilters({ ...filters, dateTo: value })
                    }
                    className="max-w-xs"
                />

                <Button
                    color="danger"
                    variant="flat"
                    onPress={() =>
                        setFilters({
                            invoiceNo: "",
                            customerName: "",
                            dateFrom: "",
                            dateTo: "",
                        })
                    }
                >
                    Reset
                </Button>
            </div>




            <Table isStriped
                aria-label="Invoices table"
                sortDescriptor={list.sortDescriptor}
                onSortChange={list.sort}
            >
                <TableHeader>
                    <TableColumn key="invoice_no" allowsSorting>
                        Invoice #
                    </TableColumn>
                    <TableColumn key="invoice_date" allowsSorting>
                        Date
                    </TableColumn>
                    <TableColumn key="total_amount" allowsSorting>
                        Total Amount
                    </TableColumn>
                    <TableColumn key="customer" allowsSorting>
                        Customer
                    </TableColumn>
                    <TableColumn key="car" allowsSorting>
                        Car
                    </TableColumn>
                    <TableColumn key="actions">
                        Actions
                    </TableColumn>
                </TableHeader>

                <TableBody
                    isLoading={isLoading}
                    items={list.items}
                    loadingContent={<Spinner label="Loading invoices..." />}
                >
                    {(invoice) => (
                        <TableRow key={invoice.id}>
                            <TableCell>{invoice.invoice_no}</TableCell>
                            <TableCell>{invoice.invoice_date}</TableCell>
                            <TableCell>
                                {Number(invoice.total_amount).toFixed(2)}
                            </TableCell>
                            <TableCell>{invoice.customer.name}</TableCell>
                            <TableCell>{invoice.car.model_name}</TableCell>
                            <TableCell>
                                <Button
                                    size="md"
                                    color="primary"
                                    onPress={() => navigate(`/invoices/${invoice.id}`)}
                                >
                                    View
                                </Button>
                            </TableCell>
                        </TableRow>
                    )}
                </TableBody>
            </Table>
        </div>
    );
}
