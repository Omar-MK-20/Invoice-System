import { Link, Navbar, NavbarBrand, NavbarContent, NavbarItem } from "@heroui/react";

function NavBar()
{
    return (
        <Navbar isBordered>
            <NavbarBrand>
                <p className="font-bold text-inherit ml-2">Invoice System</p>
            </NavbarBrand>
            <NavbarContent justify="end">
                <NavbarItem>
                    <Link href="/">Home</Link>
                </NavbarItem>
            </NavbarContent>
        </Navbar>
    );
}

export default NavBar;