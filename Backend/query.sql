-- Active: 1766933187103@@127.0.0.1@3306@invoice_system_db
CREATE DATABASE Invoice_System_DB;

USE Invoice_System_DB;

DROP DATABASE Invoice_System_DB;


SELECT customers.id, customers.name, customers.email, customers.phone, cars.id AS id_1, cars.model_name, cars.chassis_no, cars.motor_no, cars.plate_no, cars.registration_date, cars.meter_reading, cars.customer_id
FROM customers LEFT OUTER JOIN cars ON customers.id = cars.customer_id;

DELETE FROM cars;
DELETE FROM customers;





-- ===================================================


-- Insert Customers (20 records)
INSERT INTO `customers` (`name`, `email`, `phone`) VALUES
('Ahmed Hassan', 'ahmed.hassan@example.com', '+201012345678'),
('Mona Ali', 'mona.ali@example.com', '+201112345678'),
('Karim Mahmoud', 'karim.m@example.com', '+201512345678'),
('Yasmine Saleh', 'yasmine.s@example.com', '+201012345679'),
('Omar Ibrahim', 'omar.ibrahim@example.com', '+201112345679'),
('Layla Abdelrahman', 'layla.a@example.com', '+201512345679'),
('Hassan Kamal', 'hassan.k@example.com', '+201012345680'),
('Fatma Essam', 'fatma.e@example.com', '+201112345680'),
('Amir Taha', 'amir.taha@example.com', '+201512345680'),
('Nourhan Samir', 'nourhan.s@example.com', '+201012345681'),
('Youssef Farid', 'youssef.f@example.com', '+201112345681'),
('Dina Wael', 'dina.wael@example.com', '+201512345681'),
('Tarek Nabil', 'tarek.nabil@example.com', '+201012345682'),
('Sara Hisham', 'sara.hisham@example.com', '+201112345682'),
('Khaled Ashraf', 'khaled.ashraf@example.com', '+201512345682'),
('Rania Adel', 'rania.adel@example.com', '+201012345683'),
('Mahmoud Samy', 'mahmoud.samy@example.com', '+201112345683'),
('Nada Sherif', 'nada.sherif@example.com', '+201512345683'),
('Hany Magdy', 'hany.magdy@example.com', '+201012345684'),
('Mariam Osama', 'mariam.osama@example.com', '+201112345684');

-- Insert Services (10 records)
INSERT INTO `services` (`name`, `category`, `description`, `service_code`, `price`) VALUES
('Engine Oil Change', 'others', 'Complete engine oil change with synthetic oil and oil filter replacement.', 'SRV-OIL-001', 350.75),
('Brake Pad Replacement', 'manufacturing', 'Replace front and rear brake pads, inspect brake discs.', 'SRV-BRK-002', 800.00),
('Air Filter Replacement', 'spare_parts', 'Replace cabin and engine air filters.', 'SRV-AFL-003', 150.50),
('Full Car Wash', 'others', 'Complete exterior wash and interior vacuuming.', 'SRV-WSH-004', 250.00),
('Transmission Fluid Change', 'manufacturing', 'Drain and replace transmission fluid.', 'SRV-TRF-005', 1200.00),
('Battery Replacement', 'spare_parts', 'Replace car battery and test charging system.', 'SRV-BAT-006', 650.25),
('Wheel Alignment', 'manufacturing', 'Four-wheel alignment and balancing service.', 'SRV-WAL-007', 300.00),
('Spark Plug Replacement', 'spare_parts', 'Replace all spark plugs for improved engine performance.', 'SRV-SPK-008', 420.75),
('AC System Recharge', 'others', 'Recharge air conditioning system with refrigerant.', 'SRV-ACR-009', 500.00),
('Timing Belt Replacement', 'manufacturing', 'Replace timing belt and inspect related components.', 'SRV-TBR-010', 1500.00);

-- Insert Cars (35 records)
INSERT INTO `cars` (`model_name`, `chassis_no`, `motor_no`, `plate_no`, `registration_date`, `meter_reading`, `customer_id`) VALUES
('Toyota Corolla', 'JTDKB20U203000001', '1NZFE123456A', 'ABC-123', '2022-03-15', 45000, 1),
('Hyundai Elantra', 'KMHDN45D203000002', 'G4FG234567B', 'DEF-456', '2021-07-22', 52000, 2),
('Nissan Sunny', 'SJNFDAZE3U2100003', 'HR12345678C', 'GHI-789', '2020-11-30', 78000, 3),
('Chevrolet Optra', 'KLATF08Y203000004', 'F16D345678D', 'JKL-012', '2019-05-10', 112000, 4),
('Kia Cerato', 'KNAFX6A8X05300005', 'G4FC456789E', 'MNO-345', '2023-01-18', 18500, 5),
('Toyota Yaris', 'JTDJP3MV203000006', '1NR567890F', 'PQR-678', '2022-09-05', 32000, 6),
('Hyundai Accent', 'KMHCN45C203000007', 'G4EC567891G', 'STU-901', '2021-12-14', 41000, 7),
('Renault Symbol', 'VF1JA0A0523000008', 'K4J678912H', 'VWX-234', '2020-08-25', 67000, 8),
('Skoda Octavia', 'TMBJG9NE203000009', 'EA88878913I', 'YZA-567', '2023-04-30', 12500, 9),
('Peugeot 301', 'VF3YC5HZ203000010', 'EC5789101J', 'BCD-890', '2022-06-12', 29500, 10),
('Toyota Corolla', 'JTDKB20U203000011', '1NZFE123456B', 'EFG-123', '2021-10-08', 58000, 11),
('Hyundai Elantra', 'KMHDN45D203000012', 'G4FG234567C', 'HIJ-456', '2020-04-17', 89000, 12),
('Nissan Sunny', 'SJNFDAZE3U2100013', 'HR12345678D', 'KLM-789', '2019-11-23', 124000, 13),
('Chevrolet Aveo', 'KL1TD526203000014', 'F14D345678E', 'NOP-012', '2023-02-28', 9500, 14),
('Kia Picanto', 'KNADE123203000015', 'G3LA456789F', 'QRS-345', '2022-05-19', 27000, 15),
('Toyota Camry', '4T1BF1FK203000016', '2AR789012G', 'TUV-678', '2021-03-07', 63000, 16),
('Hyundai Tucson', 'KM8J3CA4623000017', 'G4KH567891H', 'WXY-901', '2020-09-14', 72000, 17),
('Nissan X-Trail', 'JN8AS5MV203000018', 'QR2589101I', 'ZAB-234', '2019-07-03', 105000, 18),
('Mitsubishi Lancer', 'JA3AJ76E203000019', '4G1891012J', 'CDE-567', '2023-08-11', 8400, 19),
('Skoda Fabia', 'TMBJG25J203000020', 'EA11178913K', 'FGH-890', '2022-11-29', 23000, 1),
('Toyota Corolla', 'JTDKB20U203000021', '1NZFE123456C', 'IJK-123', '2021-06-15', 54000, 2),
('Hyundai Elantra', 'KMHDN45D203000022', 'G4FG234567D', 'LMN-456', '2020-02-28', 81000, 3),
('Nissan Sunny', 'SJNFDAZE3U2100023', 'HR12345678E', 'OPQ-789', '2019-10-05', 118000, 4),
('Chevrolet Optra', 'KLATF08Y203000024', 'F16D345678F', 'RST-012', '2023-03-22', 7600, 5),
('Kia Cerato', 'KNAFX6A8X05300025', 'G4FC456789G', 'UVW-345', '2022-08-17', 31000, 6),
('Toyota Yaris', 'JTDJP3MV203000026', '1NR567890H', 'XYZ-678', '2021-05-04', 49000, 7),
('Hyundai Accent', 'KMHCN45C203000027', 'G4EC567891I', 'ABC-901', '2020-12-21', 69000, 8),
('Renault Logan', 'VF1JA0A0523000028', 'K7M678912J', 'DEF-234', '2019-08-08', 98000, 9),
('Skoda Rapid', 'TMBJG9NE203000029', 'EA88878913L', 'GHI-567', '2023-09-30', 5200, 10),
('Peugeot 208', 'VF3YC5HZ203000030', 'EC5789101M', 'JKL-890', '2022-04-13', 34000, 11),
('Toyota Corolla', 'JTDKB20U203000031', '1NZFE123456D', 'MNO-123', '2021-01-26', 61000, 12),
('Hyundai Elantra', 'KMHDN45D203000032', 'G4FG234567E', 'PQR-456', '2020-07-09', 85000, 13),
('Nissan Sunny', 'SJNFDAZE3U2100033', 'HR12345678F', 'STU-789', '2019-03-18', 131000, 14),
('Chevrolet Aveo', 'KL1TD526203000034', 'F14D345678G', 'VWX-012', '2023-06-05', 11300, 15),
('Kia Picanto', 'KNADE123203000035', 'G3LA456789H', 'YZA-345', '2022-10-24', 28500, 16);

-- Insert Invoices (15 records)
INSERT INTO `invoices` (`reception_engineer`, `invoice_no`, `invoice_date`, `created_at`, `total_amount`, `customer_id`, `car_id`) VALUES
('Omar Mohamed', 'INV-2023-001', '2023-10-15', '2023-10-15T10:30:00+02:00', 1828.00, 1, 1),
('Ahmed Samir', 'INV-2023-002', '2023-10-20', '2023-10-20T14:45:00+02:00', 1350.00, 2, 2),
('Mohamed Ali', 'INV-2023-003', '2023-11-05', '2023-11-05T11:15:00+02:00', 1577.75, 3, 3),
('Youssef Hany', 'INV-2023-004', '2023-11-12', '2023-11-12T16:20:00+02:00', 1050.00, 4, 4),
('Omar Mohamed', 'INV-2023-005', '2023-11-25', '2023-11-25T09:45:00+02:00', 2450.25, 5, 5),
('Ahmed Samir', 'INV-2023-006', '2023-12-03', '2023-12-03T13:30:00+02:00', 900.00, 6, 6),
('Mohamed Ali', 'INV-2023-007', '2023-12-10', '2023-12-10T15:10:00+02:00', 1918.50, 7, 7),
('Youssef Hany', 'INV-2023-008', '2023-12-18', '2023-12-18T11:55:00+02:00', 1700.00, 8, 8),
('Omar Mohamed', 'INV-2023-009', '2024-01-05', '2024-01-05T10:00:00+02:00', 1270.75, 9, 9),
('Ahmed Samir', 'INV-2023-010', '2024-01-12', '2024-01-12T14:20:00+02:00', 3150.00, 10, 10),
('Mohamed Ali', 'INV-2024-001', '2024-02-01', '2024-02-01T16:45:00+02:00', 1850.50, 11, 11),
('Youssef Hany', 'INV-2024-002', '2024-02-10', '2024-02-10T12:30:00+02:00', 2400.00, 12, 12),
('Omar Mohamed', 'INV-2024-003', '2024-02-15', '2024-02-15T09:15:00+02:00', 1520.25, 13, 13),
('Ahmed Samir', 'INV-2024-004', '2024-02-22', '2024-02-22T15:40:00+02:00', 1950.00, 14, 14),
('Mohamed Ali', 'INV-2024-005', '2024-03-01', '2024-03-01T11:25:00+02:00', 2780.75, 15, 15);

-- Insert Invoice Items (40 records)
INSERT INTO `invoice_items` (`quantity`, `price`, `discount`, `total_price`, `invoice_id`, `service_id`) VALUES
-- Invoice 1 items
(2, 350.75, 0, 701.50, 1, 1),
(1, 800.00, 50, 750.00, 1, 2),
(3, 150.50, 25, 376.50, 1, 3),
-- Invoice 2 items
(1, 250.00, 0, 250.00, 2, 4),
(1, 1200.00, 100, 1100.00, 2, 5),
-- Invoice 3 items
(1, 350.75, 0, 350.75, 3, 1),
(2, 800.00, 100, 1500.00, 3, 2),
(1, 150.50, 0, 150.50, 3, 3),
(1, 250.00, 25, 225.00, 3, 4),
-- Invoice 4 items
(1, 1200.00, 150, 1050.00, 4, 5),
-- Invoice 5 items
(1, 650.25, 0, 650.25, 5, 6),
(2, 300.00, 50, 550.00, 5, 7),
(1, 420.75, 0, 420.75, 5, 8),
(2, 500.00, 150, 850.00, 5, 9),
-- Invoice 6 items
(3, 300.00, 0, 900.00, 6, 7),
-- Invoice 7 items
(2, 350.75, 0, 701.50, 7, 1),
(1, 650.25, 0, 650.25, 7, 6),
(1, 420.75, 0, 420.75, 7, 8),
(1, 150.50, 15, 135.50, 7, 3),
-- Invoice 8 items
(1, 1500.00, 0, 1500.00, 8, 10),
(1, 250.00, 50, 200.00, 8, 4),
-- Invoice 9 items
(1, 350.75, 0, 350.75, 9, 1),
(1, 150.50, 0, 150.50, 9, 3),
(2, 250.00, 30, 470.00, 9, 4),
(1, 300.00, 0, 300.00, 9, 7),
-- Invoice 10 items
(2, 1500.00, 150, 2850.00, 10, 10),
(1, 300.00, 0, 300.00, 10, 7),
-- Invoice 11 items
(1, 800.00, 0, 800.00, 11, 2),
(1, 150.50, 0, 150.50, 11, 3),
(1, 500.00, 0, 500.00, 11, 9),
(1, 400.00, 0, 400.00, 11, 8), -- Note: price different from service price (420.75)
-- Invoice 12 items
(1, 1200.00, 0, 1200.00, 12, 5),
(1, 650.25, 50, 600.25, 12, 6),
(2, 300.00, 0, 600.00, 12, 7),
-- Invoice 13 items
(1, 350.75, 0, 350.75, 13, 1),
(1, 420.75, 0, 420.75, 13, 8),
(1, 500.00, 50, 450.00, 13, 9),
(1, 300.00, 0, 300.00, 13, 7),
-- Invoice 14 items
(1, 800.00, 100, 700.00, 14, 2),
(1, 650.25, 0, 650.25, 14, 6),
(2, 300.00, 0, 600.00, 14, 7),
-- Invoice 15 items
(1, 1500.00, 0, 1500.00, 15, 10),
(1, 650.25, 0, 650.25, 15, 6),
(1, 420.75, 0, 420.75, 15, 8),
(1, 250.00, 40, 210.00, 15, 4);







