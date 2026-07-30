import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Workspace from "./pages/Workspace"

export default function AppRoutes() {
    return (
        <Routes>
            <Route
                path="/"
                element={<Home />}
            />
            <Route
                path = "/workspace"
                element={<Workspace/>}
            />
        </Routes>
    );
}