CREATE DATABASE Invoice_System_DB;

USE Invoice_System_DB;

DROP DATABASE Invoice_System_DB;


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

-- Insert Cars (35 records)
-- Note: Customer IDs 1-20 correspond to the customers inserted above
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





SELECT customers.id, customers.name, customers.email, customers.phone, cars.id AS id_1, cars.model_name, cars.chassis_no, cars.motor_no, cars.plate_no, cars.registration_date, cars.meter_reading, cars.customer_id
FROM customers LEFT OUTER JOIN cars ON customers.id = cars.customer_id;

DELETE FROM services;
