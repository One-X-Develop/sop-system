import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import SopList from "./pages/SopList";
import SopDetail from "./pages/SopDetail";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/sops" element={<SopList />} />
      <Route path="/sops/:id" element={<SopDetail />} />
    </Routes>
  </BrowserRouter>,
);
