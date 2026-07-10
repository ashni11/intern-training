import {
  createRootRoute,
  createRoute,
  createRouter,
  Outlet,
} from "@tanstack/react-router";

import Home from "../Components/Home/Home";
import UserForm from "../Components/User/UserForm";
import SignUp from "../Components/Auth/SignUp";
import SignIn from "../Components/Auth/SignIn";

function RootLayout() {
  return <Outlet />;
}

const rootRoute = createRootRoute({
  component: RootLayout,
});

const homeRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: Home,
});

const userFormRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/user-form",
  component: UserForm,
});

const signUpRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/signup",
  component: SignUp,
});

const signInRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/signin",
  component: SignIn,
});

const routeTree = rootRoute.addChildren([
  homeRoute,
  userFormRoute,
  signUpRoute,
  signInRoute,
]);

export const router = createRouter({
  routeTree,
});