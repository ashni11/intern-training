import {
  createRootRoute,
  createRoute,
  createRouter,
  Outlet,
} from "@tanstack/react-router";

import Home from "../Components/Form/Home";
import UserForm from "../Components/Form/UserForm";

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

const routeTree = rootRoute.addChildren([homeRoute, userFormRoute]);
export const router = createRouter({ routeTree });