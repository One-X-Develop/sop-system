import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getSops } from "../api";

type Sop = { id: number; title: string };

export default function SopList() {
  const [data, setData] = useState<Sop[]>([]);

  useEffect(() => {
    getSops().then(r => setData(r.data)).catch(console.error);
  }, []);

  return (
    <>
      <h1>SOP 列表页</h1>
      <ul>
        {data.map(s => (
          <li key={s.id}>
            <Link to={`/sops/${s.id}`}>{s.title}</Link>
          </li>
        ))}
      </ul>
    </>
  );
}
