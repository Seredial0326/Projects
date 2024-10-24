public class Pelicula extends Articulo  {
    public String Estudio;
    public String Clasificacion;

    public Pelicula(){
        super();
    }

    public Pelicula(String nombre, int cantidad, int duracion, String clasificacion, String estudio){
        super(nombre, cantidad, duracion);
        this.Estudio = estudio;
        this.Clasificacion = clasificacion;
    }

    @Override
    public void CalcularPrecio(){
        this.precio = this.duracion * 1.35;
    }

    @Override
    public void RetirardelStock(){
        this.Cantidad -= cantidadselec;
    }

    public String getEstudio() {
        return Estudio;
    }
    public void setEstudio(String estudio) {
        this.Estudio = estudio;
    }

    public String getClasificacion() {
        return Clasificacion;
    }
    public void setClasificacion(String clasificacion) {
        this.Clasificacion = clasificacion;
    }
}
