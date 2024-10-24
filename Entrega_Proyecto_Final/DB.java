import java.sql.*;
import java.util.ArrayList;


public class DB {
    public Connection conexion;
    public void CrearConexion(){
        try {
            conexion = DriverManager.getConnection(
                "jdbc:mysql://127.0.0.1:3306/proyecto?user=root&password=Sere2603");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public ArrayList<Cancion> GetDatosCanciones(){
        String consulta = "SELECT * FROM Canciones;";
        ArrayList <Cancion> canciones = new ArrayList<Cancion>();

        try {
            Statement stmt = conexion.createStatement();
            ResultSet resultado = stmt.executeQuery(consulta);

            while (resultado.next()) {
                Cancion cancion = new Cancion();
                cancion.setNombre(resultado.getString("nombre"));
                cancion.setCantidad(resultado.getInt("cantidad"));
                cancion.setDisponible(resultado.getBoolean("disponible"));
                cancion.setDuracion(resultado.getInt("duracion"));
                cancion.setPrecio(resultado.getInt("precio"));
                cancion.setArtista(resultado.getString("banda"));
                cancion.setOyentes(resultado.getInt("oyentes"));
                cancion.setAlbum(resultado.getString("album"));

                canciones.add(cancion);
            }
        } catch (SQLException e) {
            System.out.println("Error de conexión: " + e.getMessage());
        }

        return canciones;
    }

    public void agregarDatosCanciones(ArrayList<Cancion> canciones)
    {
        for(Cancion i: canciones){
            String instruccionSql = "INSERT INTO Canciones(nombre, cantidad, disponible, duracion, precio, banda, oyentes, album)" + 
            "values('" + i.getNombre() + "'," + i.getCantidad() + "," + i.getDisponible() + "," + i.getDuracion() + "," + 
            i.getPrecio() + ", '" + i.getArtista() + "', " + i.getOyentes() + ", '" + i.getAlbum() + "');";

            try
            {
                Statement stmt = conexion.createStatement();
                stmt.executeUpdate(instruccionSql);
            }
            catch (SQLException e)
            {
                System.out.println("Error de conexión: " + e.getMessage());
            }
        }
    }

    public ArrayList<Pelicula> GetDatosPeliculas(){
        String consulta = "SELECT * FROM Peliculas;";
        ArrayList <Pelicula> peliculas = new ArrayList<Pelicula>();

        try {
            Statement stmt = conexion.createStatement();
            ResultSet resultado = stmt.executeQuery(consulta);

            while (resultado.next()) {
                Pelicula pelicula = new Pelicula();
                pelicula.setNombre(resultado.getString("nombre"));
                pelicula.setCantidad(resultado.getInt("cantidad"));
                pelicula.setDisponible(resultado.getBoolean("disponible"));
                pelicula.setDuracion(resultado.getInt("duracion"));
                pelicula.setPrecio(resultado.getInt("precio"));
                pelicula.setEstudio(resultado.getString("estudio"));
                pelicula.setClasificacion(resultado.getString("clasificacion"));

                peliculas.add(pelicula);
            }
        } catch (SQLException e) {
            System.out.println("Error de conexión: " + e.getMessage());
        }

        return peliculas;
    }

    public void agregarDatosPeliculas(ArrayList<Pelicula> peliculas)
    {
        for(Pelicula i: peliculas){
            String instruccionSql = "INSERT INTO Peliculas(nombre, cantidad, disponible, duracion, precio, estudio, clasificacion)" + 
            "values('" + i.getNombre() + "'," + i.getCantidad() + "," + i.getDisponible() + "," + i.getDuracion() + "," + 
            i.getPrecio() + ", '" + i.getEstudio() + "', '" + i.getClasificacion() + "');";

            try
            {
                Statement stmt = conexion.createStatement();
                stmt.executeUpdate(instruccionSql);
            }
            catch (SQLException e)
            {
                System.out.println("Error de conexión: " + e.getMessage());
            }
        }
    }

    public ArrayList<Videojuego> GetDatosVideojuegos(){
        String consulta = "SELECT * FROM Videojuegos;";
        ArrayList <Videojuego> videojuegos = new ArrayList<Videojuego>();

        try {
            Statement stmt = conexion.createStatement();
            ResultSet resultado = stmt.executeQuery(consulta);

            while (resultado.next()) {
                Videojuego juego = new Videojuego();
                juego.setNombre(resultado.getString("nombre"));
                juego.setCantidad(resultado.getInt("cantidad"));
                juego.setDisponible(resultado.getBoolean("disponible"));
                juego.setDuracion(resultado.getInt("duracion"));
                juego.setPrecio(resultado.getInt("precio"));
                juego.setJugadores(resultado.getInt("jugadores"));
                juego.setPlataforma(resultado.getString("plataforma"));

                videojuegos.add(juego);
            }
        } catch (SQLException e) {
            System.out.println("Error de conexión: " + e.getMessage());
        }

        return videojuegos;
    }

    public void agregarDatosVideojuegos(ArrayList<Videojuego> videojuegos)
    {
        for(Videojuego i: videojuegos){
            String instruccionSql = "INSERT INTO Videojuegos(nombre, cantidad, disponible, duracion, precio, jugadores, plataforma)" + 
            "values('" + i.getNombre() + "'," + i.getCantidad() + "," + i.getDisponible() + "," + i.getDuracion() + "," + 
            i.getPrecio() + "," + i.getJugadores() + ", '" + i.getPlataforma() + "');";

            try
            {
                Statement stmt = conexion.createStatement();
                stmt.executeUpdate(instruccionSql);
            }
            catch (SQLException e)
            {
                System.out.println("Error de conexión: " + e.getMessage());
            }
        }
    }

    public void GenerarTabla(){
        String borrarpeliculas = "DROP table peliculas;";
        String borrarcanciones = "DROP table canciones;";
        String borrarvideojuegos = "DROP table videojuegos;";

        String peliculas = 
            "CREATE TABLE peliculas (\n" + //
                "\tnombre varchar(255),\n" + //
                "    cantidad int,\n" + //
                "\tdisponible boolean,\n" + //
                "    duracion int,\n" + //
                "    precio double,\n" + //
                "    estudio varchar(255),\n" + //
                "    clasificacion varchar(255)\n" + //
                ");";
        String canciones =
            "CREATE TABLE canciones (\n" + //
            "\tnombre varchar(255),\n" + //
            "    cantidad int,\n" + //
            "\tdisponible boolean,\n" + //
            "    duracion int,\n" + //
            "    precio double,\n" + //
            "    banda varchar(255),\n" + //
            "    oyentes int,\n" + //
            "    album varchar(255)\n" + //
            ");";
        String videojuegos = 
            "CREATE TABLE videojuegos (\n" + //
            "\tnombre varchar(255),\n" + //
            "    cantidad int,\n" + //
            "\tdisponible boolean,\n" + //
            "    duracion int,\n" + //
            "    precio double,\n" + //
            "    jugadores int,\n" + //
            "    plataforma varchar(255)\n" + //
            ");";
        
        try
        {
            Statement stmt = conexion.createStatement();
            stmt.executeUpdate(borrarpeliculas);
            stmt.executeUpdate(peliculas);
            stmt.executeUpdate(borrarcanciones);
            stmt.executeUpdate(canciones);
            stmt.executeUpdate(borrarvideojuegos);
            stmt.executeUpdate(videojuegos);
        }
        catch (SQLException e)
        {
            System.out.println("Error de conexión: " + e.getMessage());
        }
    }

    public void attachShutDownHook(ArrayList<Cancion> canciones, ArrayList<Pelicula> peliculas, ArrayList<Videojuego> videojuegos){
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                DB db2 = new DB();
                db2.CrearConexion();
                db2.GenerarTabla();
                db2.agregarDatosCanciones(canciones);
                db2.agregarDatosPeliculas(peliculas);
                db2.agregarDatosVideojuegos(videojuegos);
            }
        });
    }
}