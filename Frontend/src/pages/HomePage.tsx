import
    {
        Button,
        Card,
        CardBody,
        CardFooter,
        CardHeader,
        Divider,
    } from "@heroui/react";
import { useNavigate } from "react-router";
import NavBar from "../components/NavBar";



export default function HomePage()
{

    const navigate = useNavigate();

    return (
        <div className="min-h-screen flex flex-col">
            <NavBar />

            {/* Main Content */}
            <main className="flex-1 px-6 py-10">
                <h1 className="text-3xl font-bold mb-2">Welcome</h1>
                <p className="text-default-500 mb-8">
                    Manage customers, services, and invoices from one place.
                </p>

                {/* Cards Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <Card>
                        <CardHeader>
                            <h3 className="text-lg font-semibold">Customers</h3>
                        </CardHeader>
                        <Divider />
                        <CardBody>
                            <p className="text-default-500">
                                View and manage all customers.
                            </p>
                        </CardBody>
                        <Divider />
                        <CardFooter>
                            <Button color="primary" fullWidth>
                                Go to Customers
                            </Button>
                        </CardFooter>
                    </Card>

                    <Card>
                        <CardHeader>
                            <h3 className="text-lg font-semibold">Services</h3>
                        </CardHeader>
                        <Divider />
                        <CardBody>
                            <p className="text-default-500">
                                Manage services and pricing.
                            </p>
                        </CardBody>
                        <Divider />
                        <CardFooter>
                            <Button color="secondary" fullWidth>
                                Go to Services
                            </Button>
                        </CardFooter>
                    </Card>

                    <Card>
                        <CardHeader>
                            <h3 className="text-lg font-semibold">Create Invoice</h3>
                        </CardHeader>
                        <Divider />
                        <CardBody>
                            <p className="text-default-500">
                                Create a new invoice quickly.
                            </p>
                        </CardBody>
                        <Divider />
                        <CardFooter>
                            <Button onPress={() => navigate('/create-invoice')} color="success" fullWidth>
                                New Invoice
                            </Button>
                        </CardFooter>
                    </Card>

                    <Card>
                        <CardHeader>
                            <h3 className="text-lg font-semibold">Invoices List</h3>
                        </CardHeader>
                        <Divider />
                        <CardBody>
                            <p className="text-default-500">
                                Browse all generated invoices.
                            </p>
                        </CardBody>
                        <Divider />
                        <CardFooter>
                            <Button onPress={() => navigate('/invoices')} color="warning" fullWidth>
                                    View Invoices
                            </Button>
                        </CardFooter>
                    </Card>
                </div>
            </main>

            {/* Footer */}
            <footer className="py-4 text-center text-sm text-default-500 border-t">
                © {new Date().getFullYear()} Omar Mohamed. All rights reserved.
            </footer>
        </div>
    );
}
