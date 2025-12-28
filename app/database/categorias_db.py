from app.database.conexion import supabase


def insertar_categoria(categoria: dict):
    return supabase.table("categorias").insert(categoria).execute()


def listar_categorias():
    return supabase.table("categorias").select("*").execute()


def actualizar_categoria(categoria_id: int, datos: dict):
    return (
        supabase
        .table("categorias")
        .update(datos)
        .eq("id", categoria_id)
        .execute()
    )


def buscar_categoria_por_nombre(nombre: str):
    return (
        supabase
        .table("categorias")
        .select("id")
        .eq("nombre", nombre)
        .execute()
    )
