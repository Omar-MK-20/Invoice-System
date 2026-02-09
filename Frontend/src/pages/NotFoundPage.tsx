import { Button } from "@heroui/react";
import { useNavigate } from "react-router";

export default function NotFoundPage()
{
    const navigate = useNavigate();

    return (
        <div className="min-h-screen flex flex-col items-center justify-center gap-4 text-center">
            <h1 className="text-5xl font-bold">404</h1>
            <p className="text-lg text-default-500">
                The page you are looking for does not exist.
            </p>

            <Button color="primary" onPress={() => navigate("/")}>
                Go Home
            </Button>
        </div>
    );
}
