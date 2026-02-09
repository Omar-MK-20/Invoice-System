export interface Car
{
    id: number;
    model_name: string;
    chassis_no: string;
    motor_no: string;
    plate_no: string;
    meter_reading: number;
    registration_date: string; // ISO date
    customer_id: number;
}