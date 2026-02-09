import { createBrowserRouter, RouterProvider } from 'react-router';
import HomePage from './pages/HomePage';
import InvoiceDetailedPage from './pages/InvoiceDetailedPage';
import InvoicesPage from './pages/InvoicesPage';
import NotFoundPage from './pages/NotFoundPage';
import CreateInvoicePage from './pages/CreateInvoicePage';


const router = createBrowserRouter([
  { path: '', element: <HomePage /> },
  { path: '/invoices', element: <InvoicesPage /> },
  { path: '/invoices/:id', element: <InvoiceDetailedPage /> },
  { path: '/create-invoice', element: <CreateInvoicePage /> },
  { path: '*', element: <NotFoundPage /> }

]);


function App()
{

  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
