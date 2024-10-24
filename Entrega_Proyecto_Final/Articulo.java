public abstract class Articulo implements IArticulo{
    public String Nombre;
    public int Cantidad;
    public boolean disponible;
    public int duracion;
    public double precio;
    public int cantidadselec;

    public abstract void CalcularPrecio();

    public Articulo(){
        Nombre = "Articulo";
        Cantidad = 0;
        disponible = false;
        duracion = 0;
        precio = 0;
    }

    public Articulo(String nombre, int cantidad, int duracion){
        this.Nombre = nombre;
        this.Cantidad = cantidad;
        if(cantidad != 0){
            this.disponible = true;
        }else{
            this.disponible = false;
        }
        this.duracion = duracion;
    }

    public String getNombre() {
        return Nombre;
    }
    public void setNombre(String nombre) {
        this.Nombre = nombre;
    }

    public int getCantidad() {
        return Cantidad;
    }
    public void setCantidad(int cantidad) {
        this.Cantidad = cantidad;
    }

    public int getCantidadSelec() {
        return cantidadselec;
    }
    public void setCantidadSelec(int cantidad) {
        this.cantidadselec = cantidad;
    }

    public boolean getDisponible() {
        return disponible;
    }
    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }

    public int getDuracion() {
        return duracion;
    }
    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public double getPrecio() {
        return this.precio;
    }
    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public void RetirardelStock(){
        this.Cantidad -= this.cantidadselec;
    }
}
