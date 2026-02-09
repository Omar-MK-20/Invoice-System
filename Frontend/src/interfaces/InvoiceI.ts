import type { Car } from "./CarI";
import type { Customer } from "./CustomerI";
import type { Service } from "./ServiceI";

export interface Invoice
{
    id: number;
    invoice_no: string;
    invoice_date: string;
    created_at: string;
    reception_engineer: string;
    total_amount: number;

    customer_id: number;
    car_id: number;

    customer: Customer;
    car: Car;
}

export interface InvoiceItem
{
    id: number;
    invoice_id: number;
    service_id: number;
    quantity: number;
    price: number;
    discount: number;
    total_price: number;
    service: Service;
}

export interface InvoiceWithItems extends Invoice
{
    invoice_items: InvoiceItem[];
}

export interface InvoicesResponse
{
    message: string;
    invoices: Invoice[];
}


export interface SingleInvoiceResponse
{
    message: string;
    invoice: InvoiceWithItems;
}