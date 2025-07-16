import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getSop } from "../api";

type Sop = { id: number; title: string; content: string };

export default function SopDetail() {
  const { id } = useParams();
  const [sop, setSop] = useState<Sop | null>(null);

  useEffect(() => {
    id && getSop(id).then(r => setSop(r.data)).catch(console.error);
  }, [id]);

  if (!sop) return <p>加载中…</p>;

  return (
    <>
      <h1>{sop.title}</h1>
      <pre>{sop.content}</pre>
    </>
  );
}
