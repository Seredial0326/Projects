public class Videojuego extends Articulo {
    public int jugadores;
    public String plataforma;

    public Videojuego(){
        super();
    }

    public Videojuego(String nombre, int cantidad, int duracion, int jugadores, String plataforma){
        super(nombre, cantidad, duracion);
        this.jugadores = jugadores;
        this.plataforma = plataforma;
    }

    @Override
    public void CalcularPrecio(){
        this.precio = this.jugadores*1000;
    }

    @Override
    public void RetirardelStock(){
        this.Cantidad -= cantidadselec;
    }

    public String getPlataforma() {
        return plataforma;
    }
    public void setPlataforma(String plataforma) {
        this.plataforma = plataforma;
    }

    public int getJugadores() {
        return jugadores;
    }
    public void setJugadores(int jugadores) {
        this.jugadores = jugadores;
    }
}
