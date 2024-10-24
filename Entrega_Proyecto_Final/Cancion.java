public class Cancion extends Articulo {
    public String banda;
    public int Oyentes;
    public String Album;

    public Cancion(){
        super();
    }

    public Cancion(String nombre, int cantidad, int duracion, String album, String banda, int oyentes){
        super(nombre, cantidad, duracion);
        this.banda = banda;
        this.Album = album;
        this.Oyentes = oyentes;
    }

    @Override
    public void CalcularPrecio(){
        this.precio = this.duracion*.35;
    }

    @Override
    public void RetirardelStock(){
        this.Cantidad -= cantidadselec;
    }

    public String getArtista() {
        return banda;
    }
    public void setArtista(String banda) {
        this.banda = banda;
    }

    public String getAlbum() {
        return Album;
    }
    public void setAlbum(String album) {
        this.Album = album;
    }

    public int getOyentes() {
        return Oyentes;
    }
    public void setOyentes(int oyentes) {
        this.Oyentes = oyentes;
    }
}
