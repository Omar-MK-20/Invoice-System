export interface Service
{
    id: number;
    name: string;
    description: string;
    category: "manufacturing" | "spare_parts" | "others";
    service_code: string;
    price: number;
}