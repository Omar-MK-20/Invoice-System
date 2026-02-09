import * as z from "zod";

export const invoiceItemSchema = z.object({
  service_id: z.number(),
  quantity: z.number().min(1),
  discount: z.number().min(0).optional(),
});

export const createInvoiceSchema = z.object({
  invoice_no: z.string().min(1),
  invoice_date: z.string(),
  customer_name: z.string().min(3),
  car_id: z.number(),
  invoice_items: z.array(invoiceItemSchema).min(1),
});

export type CreateInvoiceForm = z.infer<typeof createInvoiceSchema>;
