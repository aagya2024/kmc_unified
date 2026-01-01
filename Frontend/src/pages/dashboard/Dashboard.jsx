// src/pages/dashboard/Dashboard.jsx
import UserDashboard from "./UserDashboard";
import SuperAdminDashboard from "./SuperAdminDashboard";
import WardAdminDashboard from "./WardAdminDashboard";
import DepartmentAdminDashboard from "./DepartmentAdminDashboard";
import Unauthorized from "@/pages/common/Unauthorized";
import { useAuth } from "@/contexts/useAuth";

const Dashboard = () => {
  const { role } = useAuth();

  switch (role) {
    case "super_admin":
      return <SuperAdminDashboard />;

    case "ward_admin":
      return <WardAdminDashboard />;

    case "depaartment_admin":
      return <DepartmentAdminDashboard />;

    case "user":
      return <UserDashboard />;

    default:
      return <Unauthorized />;
  }
};

export default Dashboard;
