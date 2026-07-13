import {
  createRootRoute,
  createRoute,
  createRouter,
  Outlet,
} from "@tanstack/react-router";

import SignIn from "../Components/Auth/SignIn";
import SignUp from "../Components/Auth/SignUp";
import Home from "../Components/Home/Home";
import CreateUser from "../Components/User/CreateUser";
import EditUser from "../Components/User/EditUser";

const rootRoute = createRootRoute({
  component: () => <Outlet />,
});

const signinRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: SignIn,
});

const signupRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/signup",
  component: SignUp,
});

const homeRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/home",
  component: Home,
});

const createUserRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/create",
  component: CreateUser,
});

const editUserRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/edit/$id",
  component: EditUser,
});

const routeTree = rootRoute.addChildren([
  signinRoute,
  signupRoute,
  homeRoute,
  createUserRoute,
  editUserRoute,
]);

export const router = createRouter({
  routeTree,
});

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}