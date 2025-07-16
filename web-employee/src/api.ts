import axios from "axios";

const api = axios.create({ baseURL: "/api" });

export const getSops = () => api.get("/sops");          // 列表
export const getSop  = (id: string) => api.get(`/sops/${id}`); // 详情
