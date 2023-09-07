// PrivateRoute.js
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from './auth/AuthProvider'; // Import your authentication context or logic here

const PrivateRoute = () => {
  const { user } = useAuth(); // Assuming you have a user object from your authentication context

  // If the user is authenticated, return an outlet that will render child elements
  // If not, return a Navigate element to redirect to the login page
  return user ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoute;
