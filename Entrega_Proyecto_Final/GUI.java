import javax.swing.*;
import javax.swing.table.*;

import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class GUI {
    public static void main(String[] args) {
        ArrayList<Pelicula> Peliculas = new ArrayList<Pelicula>();
        ArrayList<Cancion> Canciones = new ArrayList<Cancion>();
        ArrayList<Videojuego> Videojuegos = new ArrayList<Videojuego>();
        ArrayList<Articulo> Compras = new ArrayList<Articulo>();

        DB db1 = new DB();
        db1.CrearConexion();
        for(Pelicula i: db1.GetDatosPeliculas()){
            Peliculas.add(i);
        }
        for(Cancion i: db1.GetDatosCanciones()){
            Canciones.add(i);
        }
        for(Videojuego i: db1.GetDatosVideojuegos()){
            Videojuegos.add(i);
        }

        JFrame frame = new JFrame("Tienda");
        frame.setLayout(null);
        frame.setSize(1600, 800);
        frame.getContentPane().setBackground(new Color(95,136,201));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel blockbuster = new JLabel();
        JButton bienvenida = new JButton("¿Cómo funciona?");
        ImageIcon icono = new ImageIcon("C:\\Users\\sered\\OneDrive\\Documentos\\Java\\Entrega_Proyecto_Final\\Logo3.png");

        ImageIcon iconPelicula = new ImageIcon("C:\\Users\\sered\\OneDrive\\Documentos\\Java\\Entrega_Proyecto_Final\\Cine.jpg");
        ImageIcon iconoCancion = new ImageIcon("C:\\Users\\sered\\OneDrive\\Documentos\\Java\\Entrega_Proyecto_Final\\Musica.jpg");
        ImageIcon iconoVJ = new ImageIcon("C:\\Users\\sered\\OneDrive\\Documentos\\Java\\Entrega_Proyecto_Final\\Juego.jpg");

        blockbuster.setIcon(icono);

        blockbuster.setBounds(1,10,1300,700);
        bienvenida.setBounds(1140, 600, 170, 25);

        bienvenida.setForeground(new Color(8,2,117));

        frame.add(blockbuster);
        frame.add(bienvenida);

        bienvenida.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                JOptionPane.showMessageDialog(frame, "Bienvenido a Blockbuster 2.0, aquí podrás:\n1. Agregar películas, canciones y/o videojuegos\n2. Comprar cualquiera de los elementos antes mencionados\n 3. Ver el inventario de la tienda", "Bienvenida", 1);
            }
        });

        JButton Agregar = new JButton("Agregar");
        JButton Comprar = new JButton("Comprar");
        JButton Reporte = new JButton("Inventario");

        Agregar.setBounds(1140,125,170,25);
        Comprar.setBounds(1140, 275, 170, 25);
        Reporte.setBounds(1140, 425, 170, 25);

        Agregar.setBackground(new Color(255,214,102));
        Comprar.setBackground(new Color(255,214,102));
        Reporte.setBackground(new Color(255,214,102));
        bienvenida.setBackground(new Color(5,54,133));

        Agregar.setForeground(new Color(5,54,133));
        Comprar.setForeground(new Color(5,54,133));
        Reporte.setForeground(new Color(5,54,133));
        bienvenida.setForeground(new Color(255,214,102));

        frame.add(Agregar);
        frame.add(Comprar);
        frame.add(Reporte);

        Agregar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFrame Frame2 = new JFrame("Agregar");
                Frame2.setSize(650, 300);

                JPanel panelprinc2 = new JPanel(new GridLayout(1,3));
                Frame2.setContentPane(panelprinc2);

                Frame2.setResizable(false);

                JPanel panelfr1 = new JPanel(new FlowLayout());
                JPanel panelfr2 = new JPanel(new FlowLayout());
                JPanel panelfr3 = new JPanel(new FlowLayout());

                JButton cancion = new JButton();
                JButton pelicula = new JButton();
                JButton juego = new JButton();

                cancion.setMinimumSize(new Dimension(40,20));
                cancion.setMaximumSize(new Dimension(300,250));
                cancion.setPreferredSize(new Dimension(150,150));

                pelicula.setMinimumSize(new Dimension(40,20));
                pelicula.setMaximumSize(new Dimension(300,250));
                pelicula.setPreferredSize(new Dimension(150,150));

                juego.setMinimumSize(new Dimension(40,20));
                juego.setMaximumSize(new Dimension(300,250));
                juego.setPreferredSize(new Dimension(150,150));

                cancion.setIcon(iconoCancion);
                pelicula.setIcon(iconPelicula);
                juego.setIcon(iconoVJ);

                JLabel peli = new JLabel("Películas");
                peli.setForeground(new Color(12,6,125));
                peli.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel mus = new JLabel("Canciones");
                mus.setForeground(new Color(12,6,125));
                mus.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel jug = new JLabel("Videojuegos");
                jug.setForeground(new Color(12,6,125));
                jug.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel op = new JLabel("¿Cuál elemento desea agregar?");
                op.setForeground(new Color(189,4,4));
                op.setFont(new Font("Calibri Light",Font.PLAIN,16));

                panelfr1.add(pelicula);
                panelfr1.add(peli);
                panelfr2.add(cancion);
                panelfr2.add(mus);
                panelfr2.add(op);
                panelfr3.add(juego);
                panelfr3.add(jug);

                panelprinc2.add(panelfr1);
                panelprinc2.add(panelfr2);
                panelprinc2.add(panelfr3);

                Frame2.setLocationRelativeTo(frame);

                pelicula.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame Frame3 = new JFrame("Nueva Película");
                        Frame3.setSize(350, 265);
                        JPanel panelTel1 = new JPanel(new GridLayout(6,1));
                        Frame3.setContentPane(panelTel1);
                        Frame3.setResizable(false);

                        JPanel panelTel11 = new JPanel(new FlowLayout());
                        JPanel panelTel12 = new JPanel(new FlowLayout());
                        JPanel panelTel13 = new JPanel(new FlowLayout());
                        JPanel panelTel14 = new JPanel(new FlowLayout());
                        JPanel panelTel15 = new JPanel(new FlowLayout());
                        JPanel panelTel16 = new JPanel(new FlowLayout());

                        panelTel1.add(panelTel11);
                        panelTel1.add(panelTel12);
                        panelTel1.add(panelTel13);
                        panelTel1.add(panelTel14);
                        panelTel1.add(panelTel15);

                        JLabel opc1 = new JLabel("Nombre (título)");
                        JTextField nombreP = new JTextField(10);
                        panelTel11.add(opc1);
                        panelTel11.add(nombreP);

                        JLabel opc2 = new JLabel("Cantidad Stock");
                        JTextField cantidadStockP = new JTextField(10);
                        panelTel12.add(opc2);
                        panelTel12.add(cantidadStockP);

                        JLabel opc3 = new JLabel("Duración (minutos)");
                        JSpinner spinner = new JSpinner();
                        spinner.setPreferredSize(new Dimension(50,20));
                        panelTel13.add(spinner);
                        panelTel13.add(opc3);
                        panelTel13.add(spinner);

                        JLabel opc4 = new JLabel("Clasificación");
                        JTextField clasificacion = new JTextField(10);
                        panelTel14.add(opc4);
                        panelTel14.add(clasificacion);

                        JLabel opc5 = new JLabel("Estudio (o independiente)");
                        JTextField Estudio = new JTextField(10);
                        panelTel15.add(opc5);
                        panelTel15.add(Estudio);
                        
                        panelTel1.add(panelTel16);

                        JButton datos = new JButton("Agregar datos");

                        datos.addActionListener(new ActionListener() {
                            @Override
                            public void actionPerformed(ActionEvent e) {
                                try{
                                    String nombreP1 = nombreP.getText();
                                    String cantidadStockaP1 = cantidadStockP.getText();
                                    int TamañoR = (int) spinner.getValue();
                                    String clasifP1 = clasificacion.getText();
                                    String estudioP1 = Estudio.getText();

                                    int x = Integer.parseInt(cantidadStockaP1);
                                    
                                    Peliculas.add(new Pelicula(nombreP1,x,TamañoR,clasifP1,estudioP1));

                                    JOptionPane.showMessageDialog(Frame3, "Datos registrados", "Listo", 1);
                                    
                                    Frame3.setVisible(false);
                                    Frame2.setVisible(true);
                                } catch (Exception w) {
                                    JOptionPane.showMessageDialog(Frame3, "Ingresa bien los datos", "ERROR", 0);
                                }
                            }
                        });
                        panelTel16.add(datos);
                        Frame3.setLocationRelativeTo(frame);
                        Frame3.setVisible(true);
                    }
                });

                cancion.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame Frame3 = new JFrame("Nueva Canción");
                        Frame3.setSize(350, 265);
                        JPanel panelTel1 = new JPanel(new GridLayout(7,1));
                        Frame3.setContentPane(panelTel1);
                        Frame3.setResizable(false);

                        JPanel panelTel11 = new JPanel(new FlowLayout());
                        JPanel panelTel12 = new JPanel(new FlowLayout());
                        JPanel panelTel13 = new JPanel(new FlowLayout());
                        JPanel panelTel14 = new JPanel(new FlowLayout());
                        JPanel panelTel15 = new JPanel(new FlowLayout());
                        JPanel panelTel16 = new JPanel(new FlowLayout());
                        JPanel panelTel17 = new JPanel(new FlowLayout());

                        panelTel1.add(panelTel11);
                        panelTel1.add(panelTel12);
                        panelTel1.add(panelTel13);
                        panelTel1.add(panelTel14);
                        panelTel1.add(panelTel15);
                        panelTel1.add(panelTel16);

                        JLabel opc1 = new JLabel("Nombre (título)");
                        JTextField nombreP = new JTextField(10);
                        panelTel11.add(opc1);
                        panelTel11.add(nombreP);

                        JLabel opc2 = new JLabel("Cantidad Stock (disco)");
                        JTextField cantidadStockP = new JTextField(10);
                        panelTel12.add(opc2);
                        panelTel12.add(cantidadStockP);

                        JLabel opc3 = new JLabel("Duración (segundos)");
                        JSpinner spinner = new JSpinner();
                        spinner.setPreferredSize(new Dimension(50,20));
                        panelTel13.add(spinner);
                        panelTel13.add(opc3);
                        panelTel13.add(spinner);

                        JLabel opc4 = new JLabel("Oyentes mensuales");
                        JTextField oyentes = new JTextField(10);
                        panelTel14.add(opc4);
                        panelTel14.add(oyentes);

                        JLabel opc5 = new JLabel("Artista/Banda");
                        JTextField Artista1 = new JTextField(10);
                        panelTel15.add(opc5);
                        panelTel15.add(Artista1);

                        JLabel opc6 = new JLabel("Álbum (o sencillo)");
                        JTextField Album1 = new JTextField(10);
                        panelTel16.add(opc6);
                        panelTel16.add(Album1);
                        
                        panelTel1.add(panelTel17);

                        JButton datos = new JButton("Agregar datos");

                        datos.addActionListener(new ActionListener() {
                            @Override
                            public void actionPerformed(ActionEvent e) {
                                try{
                                    String nombreP1 = nombreP.getText();
                                    String cantidadStockaP1 = cantidadStockP.getText();
                                    int Duracion = (int) spinner.getValue();
                                    String oyentesC1 = oyentes.getText();
                                    String Album = Album1.getText();
                                    String Artista = Artista1.getText();

                                    int x = Integer.parseInt(cantidadStockaP1);
                                    int y = Integer.parseInt(oyentesC1);

                                    Canciones.add(new Cancion(nombreP1,x,Duracion,Album,Artista,y));

                                    JOptionPane.showMessageDialog(Frame3, "Datos registrados", "Listo", 1);

                                    Frame3.setVisible(false);
                                    Frame2.setVisible(true);
                                } catch (Exception w) {
                                    JOptionPane.showMessageDialog(Frame3, "Ingresa bien los datos", "ERROR", 0);
                                } 
                            }
                        });
                        panelTel17.add(datos);

                        Frame3.setLocationRelativeTo(frame);
                        Frame3.setVisible(true);
                    }
                });

                juego.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame Frame3 = new JFrame("Nuevo Videojuego");
                        Frame3.setSize(350, 265);
                        JPanel panelTel1 = new JPanel(new GridLayout(6,1));
                        Frame3.setContentPane(panelTel1);
                        Frame3.setResizable(false);

                        JPanel panelTel11 = new JPanel(new FlowLayout());
                        JPanel panelTel12 = new JPanel(new FlowLayout());
                        JPanel panelTel13 = new JPanel(new FlowLayout());
                        JPanel panelTel14 = new JPanel(new FlowLayout());
                        JPanel panelTel15 = new JPanel(new FlowLayout());
                        JPanel panelTel16 = new JPanel(new FlowLayout());

                        panelTel1.add(panelTel11);
                        panelTel1.add(panelTel12);
                        panelTel1.add(panelTel13);
                        panelTel1.add(panelTel14);
                        panelTel1.add(panelTel15);

                        JLabel opc1 = new JLabel("Nombre (título)");
                        JTextField nombreP = new JTextField(10);
                        panelTel11.add(opc1);
                        panelTel11.add(nombreP);

                        JLabel opc2 = new JLabel("Cantidad Stock");
                        JTextField cantidadStockP = new JTextField(10);
                        panelTel12.add(opc2);
                        panelTel12.add(cantidadStockP);

                        JLabel opc3 = new JLabel("Duración aprox. (horas)");
                        JSpinner spinner = new JSpinner();
                        spinner.setPreferredSize(new Dimension(50,20));
                        panelTel13.add(spinner);
                        panelTel13.add(opc3);
                        panelTel13.add(spinner);

                        JLabel opc4 = new JLabel("Cantidad jugadores");
                        JSpinner jugadores = new JSpinner();
                        jugadores.setPreferredSize(new Dimension(50,20));
                        panelTel14.add(opc4);
                        panelTel14.add(jugadores);

                        JLabel opc5 = new JLabel("Plataforma");
                        JTextField plataforma = new JTextField(10);
                        panelTel15.add(opc5);
                        panelTel15.add(plataforma);
                        
                        panelTel1.add(panelTel16);

                        JButton datos = new JButton("Agregar datos");

                        datos.addActionListener(new ActionListener() {
                            @Override
                            public void actionPerformed(ActionEvent e) {
                                try{
                                    String nombreP1 = nombreP.getText();
                                    String cantidadStockaP1 = cantidadStockP.getText();
                                    int TamañoR = (int) spinner.getValue();
                                    int jugJ1 = (int) jugadores.getValue();
                                    String platJ1 = plataforma.getText();

                                    int x = Integer.parseInt(cantidadStockaP1);

                                    Videojuegos.add(new Videojuego(nombreP1,x,TamañoR,jugJ1,platJ1));

                                    JOptionPane.showMessageDialog(Frame3, "Datos registrados", "Listo", 1);

                                    Frame3.setVisible(false);
                                    Frame2.setVisible(true);
                                } catch (Exception w) {
                                    JOptionPane.showMessageDialog(Frame3, "Ingresa bien los datos", "ERROR", 0);
                                }
                            }
                        });
                        panelTel16.add(datos);

                        Frame3.setLocationRelativeTo(frame);
                        Frame3.setVisible(true);
                    }
                });
                
                db1.agregarDatosPeliculas(Peliculas);
                db1.agregarDatosCanciones(Canciones);
                db1.agregarDatosVideojuegos(Videojuegos);
                Frame2.setVisible(true);
            }
        }); 

        Comprar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                JOptionPane.showMessageDialog(frame, "Primero seleccione los productos que desee comprar, y cuando este seguro de click en Comprar", "Instrucciones", 1);

                JFrame Frame4= new JFrame("Comprar");
                Frame4.setSize(650, 300);

                JPanel panelprinc2 = new JPanel(new GridLayout(1,3));
                Frame4.setContentPane(panelprinc2);

                JPanel panelfr1 = new JPanel(new FlowLayout());
                JPanel panelfr2 = new JPanel(new FlowLayout());
                JPanel panelfr3 = new JPanel(new FlowLayout());

                JButton cancion = new JButton();
                JButton pelicula = new JButton();
                JButton juego = new JButton();
                JButton selec = new JButton("Comprar");

                selec.setForeground(new Color(5,54,133));
                selec.setBackground(new Color(255,214,102));

                selec.setMinimumSize(new Dimension(40,20));
                selec.setMaximumSize(new Dimension(300,250));
                selec.setPreferredSize(new Dimension(150,40));

                cancion.setMinimumSize(new Dimension(40,20));
                cancion.setMaximumSize(new Dimension(300,250));
                cancion.setPreferredSize(new Dimension(150,150));

                pelicula.setMinimumSize(new Dimension(40,20));
                pelicula.setMaximumSize(new Dimension(300,250));
                pelicula.setPreferredSize(new Dimension(150,150));

                juego.setMinimumSize(new Dimension(40,20));
                juego.setMaximumSize(new Dimension(300,250));
                juego.setPreferredSize(new Dimension(150,150));

                cancion.setIcon(iconoCancion);
                pelicula.setIcon(iconPelicula);
                juego.setIcon(iconoVJ);

                JLabel peli = new JLabel("Películas");
                peli.setForeground(new Color(12,6,125));
                peli.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel mus = new JLabel("Canciones");
                mus.setForeground(new Color(12,6,125));
                mus.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel jug = new JLabel("Videojuegos");
                jug.setForeground(new Color(12,6,125));
                jug.setFont(new Font("Calibri Light",Font.PLAIN,16));

                panelfr1.add(cancion);
                panelfr1.add(mus);
                panelfr1.add(selec);
                panelfr2.add(pelicula);
                panelfr2.add(peli);
                panelfr3.add(juego);
                panelfr3.add(jug);

                panelprinc2.add(panelfr2);
                panelprinc2.add(panelfr1);
                panelprinc2.add(panelfr3);

                Frame4.setVisible(true);
                Frame4.setLocationRelativeTo(frame);

                pelicula.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Peliculas");   
                        frame.setLocation(175, 250);                     

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return String.class;
                                    case 4:
                                        return String.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duración (min)");
                        modelo.addColumn("Clasificación");
                        modelo.addColumn("Estudio");
                        modelo.addColumn("Seleccionar");

                        for (int i = 0; i < Peliculas.size(); i++) {
                            Object[] fila = new Object[6];
                            fila[0] = Peliculas.get(i).getNombre();
                            fila[1] = Peliculas.get(i).getCantidad();
                            fila[2] = Peliculas.get(i).getDuracion();
                            fila[3] = Peliculas.get(i).getClasificacion();
                            fila[4] = Peliculas.get(i).getEstudio();
                            fila[5] = false;
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);
                        tabla.getColumnModel().getColumn(5).setCellEditor(new DefaultCellEditor(new JCheckBox()));

                        modelo.addTableModelListener(a -> {
                            if (a.getColumn() == 5) {
                                int fila = a.getFirstRow();
                                boolean seleccionado = (boolean) modelo.getValueAt(fila, 5);
                                if (seleccionado) {
                                    Compras.add(Peliculas.get(fila));

                                    Peliculas.get(fila).CalcularPrecio();

                                    JFrame Frame3 = new JFrame();
                                    Frame3.setSize(200, 100);
                                    Frame3.setResizable(false);
                                    Frame3.setLocationRelativeTo(frame);

                                    JPanel frame3panel1 = new JPanel(new FlowLayout());
                                    Frame3.setContentPane(frame3panel1);

                                    JSpinner spinner = new JSpinner();
                                    spinner.setPreferredSize(new Dimension(50,30));
                                    frame3panel1.add(spinner);

                                    JButton cantidadframe3 = new JButton("Confirmar");
                                    
                                    cantidadframe3.addActionListener(new ActionListener() {
                                        @Override
                                        public void actionPerformed(ActionEvent e){
                                            Peliculas.get(fila).setCantidadSelec((int) spinner.getValue());
                                            if(Peliculas.get(fila).cantidadselec > Peliculas.get(fila).getCantidad()) {
                                                JOptionPane.showMessageDialog(cantidadframe3, "No puedes agregar tal cantidad al carrito pues nuestro es Stock es de tan solo: " + Peliculas.get(fila).getCantidad(), "Stock", 0);
                                            }else{
                                                JOptionPane.showMessageDialog(cantidadframe3, "Agregaste " + Peliculas.get(fila).getCantidadSelec() + " " + Peliculas.get(fila).getNombre() + " al carrito de ventas", "Carrito de Ventas", 1);
                                                Frame3.setVisible(false);
                                            }
                                        }
                                    });

                                    frame3panel1.add(cantidadframe3);

                                    Frame3.setVisible(true);
                                }
                            }
                        });

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                       
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                });

                cancion.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Canciones");                        
                        frame.setLocation(175, 250);

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return String.class;
                                    case 4:
                                        return String.class;
                                    case 5:
                                        return Integer.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duración (min)");
                        modelo.addColumn("Álbum");
                        modelo.addColumn("Banda");
                        modelo.addColumn("Oyentes");
                        modelo.addColumn("Seleccionar");

                        for (int i = 0; i < Canciones.size(); i++) {
                            Object[] fila = new Object[7];
                            fila[0] = Canciones.get(i).getNombre();
                            fila[1] = Canciones.get(i).getCantidad();
                            fila[2] = Canciones.get(i).getDuracion();
                            fila[3] = Canciones.get(i).getAlbum();
                            fila[4] = Canciones.get(i).getArtista();
                            fila[5] = Canciones.get(i).getOyentes();
                            fila[6] = false;
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);
                        tabla.getColumnModel().getColumn(5).setCellEditor(new DefaultCellEditor(new JCheckBox()));

                        modelo.addTableModelListener(a -> {
                            if (a.getColumn() == 6) {
                                int fila = a.getFirstRow();
                                boolean seleccionado = (boolean) modelo.getValueAt(fila, 6);
                                if (seleccionado) {
                                    Compras.add(Canciones.get(fila));
                                    
                                    Canciones.get(fila).CalcularPrecio();

                                    JFrame Frame3 = new JFrame();
                                    Frame3.setSize(200, 100);
                                    Frame3.setResizable(false);
                                    Frame3.setLocationRelativeTo(frame);

                                    JPanel frame3panel1 = new JPanel(new FlowLayout());
                                    Frame3.setContentPane(frame3panel1);

                                    JSpinner spinner = new JSpinner();
                                    spinner.setMinimumSize(new Dimension(70, 40));
                                    spinner.setMaximumSize(new Dimension(100, 100));
                                    spinner.setPreferredSize(new Dimension(50,30));
                                    frame3panel1.add(spinner);

                                    JButton cantidadframe3 = new JButton("Confirmar");
                                    
                                    cantidadframe3.addActionListener(new ActionListener() {
                                        @Override
                                        public void actionPerformed(ActionEvent e){
                                            Canciones.get(fila).setCantidadSelec((int) spinner.getValue());
                                            if(Canciones.get(fila).cantidadselec > Canciones.get(fila).getCantidad()) {
                                                JOptionPane.showMessageDialog(cantidadframe3, "No puedes agregar tal cantidad al carrito pues nuestro es Stock es de tan solo: " + Canciones.get(fila).getCantidad(), "Stock", 0);
                                            }else{
                                                JOptionPane.showMessageDialog(cantidadframe3, "Agregaste " + Canciones.get(fila).getCantidadSelec() + " " + Canciones.get(fila).getNombre() + " al carrito de ventas", "Carrito de Ventas", 1);
                                                Frame3.setVisible(false);
                                            }
                                        }
                                    });

                                    frame3panel1.add(cantidadframe3);

                                    Frame3.setVisible(true);
                                }
                            }
                        });

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                        
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                }); 
                
                juego.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Videojuegos");
                        frame.setLocation(175, 250);                        

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return Integer.class;
                                    case 4:
                                        return String.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duración (min)");
                        modelo.addColumn("Cantidad jugadores");
                        modelo.addColumn("Plataforma");
                        modelo.addColumn("Seleccionar");

                        for (int i = 0; i < Videojuegos.size(); i++) {
                            Object[] fila = new Object[6];
                            fila[0] = Videojuegos.get(i).getNombre();
                            fila[1] = Videojuegos.get(i).getCantidad();
                            fila[2] = Videojuegos.get(i).getDuracion();
                            fila[3] = Videojuegos.get(i).getJugadores();
                            fila[4] = Videojuegos.get(i).getPlataforma();
                            fila[5] = false;
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);
                        tabla.getColumnModel().getColumn(5).setCellEditor(new DefaultCellEditor(new JCheckBox()));

                        modelo.addTableModelListener(a -> {
                            if (a.getColumn() == 5) {
                                int fila = a.getFirstRow();
                                boolean seleccionado = (boolean) modelo.getValueAt(fila, 5);
                                if (seleccionado) {
                                    Compras.add(Videojuegos.get(fila));
                                    Videojuegos.get(fila).CalcularPrecio();


                                    JFrame Frame3 = new JFrame();
                                    Frame3.setSize(200, 100);
                                    Frame3.setResizable(false);
                                    Frame3.setLocationRelativeTo(frame);
                                    
                                    JPanel frame3panel1 = new JPanel(new FlowLayout());
                                    Frame3.setContentPane(frame3panel1);

                                    JSpinner spinner = new JSpinner();
                                    spinner.setMinimumSize(new Dimension(70, 40));
                                    spinner.setMaximumSize(new Dimension(100, 100));
                                    spinner.setPreferredSize(new Dimension(50,30));
                                    frame3panel1.add(spinner);

                                    JButton cantidadframe3 = new JButton("Confirmar");
                                    
                                    cantidadframe3.addActionListener(new ActionListener() {
                                        @Override
                                        public void actionPerformed(ActionEvent e){
                                            Videojuegos.get(fila).setCantidadSelec((int) spinner.getValue());
                                            if(Videojuegos.get(fila).cantidadselec > Videojuegos.get(fila).getCantidad()) {
                                                JOptionPane.showMessageDialog(cantidadframe3, "No puedes agregar tal cantidad al carrito pues nuestro es Stock es de tan solo: " + Videojuegos.get(fila).getCantidad(), "Stock", 0);
                                            }else{
                                                JOptionPane.showMessageDialog(cantidadframe3, "Agregaste " + Videojuegos.get(fila).getCantidadSelec() + " " + Videojuegos.get(fila).getNombre() + " al carrito de ventas", "Carrito de Ventas", 1);
                                                Frame3.setVisible(false);
                                            }
                                        }
                                    });

                                    frame3panel1.add(cantidadframe3);

                                    Frame3.setVisible(true);
                                }
                            }
                        });

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                       
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                });

                selec.addActionListener(new ActionListener() {
                    float suma = 0;
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        if (Compras.isEmpty()){
                            JOptionPane.showMessageDialog(frame, "Aún no seleccionas ningún producto", "ERROR", 0);                             
                        }else{
                            for(int i = 0; i< Compras.size(); i++){
                                Compras.get(i).RetirardelStock();
                                suma += Compras.get(i).getPrecio()*Compras.get(i).getCantidadSelec();
                                Compras.get(i).setCantidadSelec(0);
                            }
                            JOptionPane.showMessageDialog(frame, "Haga favor de pagar en caja la humilde cantidad de $"+ suma, "Comprar", 1); 
                        }
                        suma = 0;
                    }
                });
            }
        });

        Reporte.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                for(Videojuego i:Videojuegos){
                    i.CalcularPrecio();
                }
                for(Pelicula i:Peliculas){
                    i.CalcularPrecio();
                }
                for(Cancion i:Canciones){
                    i.CalcularPrecio();
                }

                JFrame Frame4= new JFrame("Inventario");
                Frame4.setSize(650, 300);

                JPanel panelprinc2 = new JPanel(new GridLayout(1,3));
                Frame4.setContentPane(panelprinc2);

                JPanel panelfr1 = new JPanel(new FlowLayout());
                JPanel panelfr2 = new JPanel(new FlowLayout());
                JPanel panelfr3 = new JPanel(new FlowLayout());

                JButton cancion = new JButton();
                JButton pelicula = new JButton();
                JButton juego = new JButton();
                JButton todos = new JButton("Ver todo");

                todos.setForeground(new Color(5,54,133));
                todos.setBackground(new Color(255,214,102));

                todos.setMinimumSize(new Dimension(40,20));
                todos.setMaximumSize(new Dimension(300,250));
                todos.setPreferredSize(new Dimension(150,40));

                cancion.setMinimumSize(new Dimension(40,20));
                cancion.setMaximumSize(new Dimension(300,250));
                cancion.setPreferredSize(new Dimension(150,150));

                pelicula.setMinimumSize(new Dimension(40,20));
                pelicula.setMaximumSize(new Dimension(300,250));
                pelicula.setPreferredSize(new Dimension(150,150));

                juego.setMinimumSize(new Dimension(40,20));
                juego.setMaximumSize(new Dimension(300,250));
                juego.setPreferredSize(new Dimension(150,150));

                cancion.setIcon(iconoCancion);
                pelicula.setIcon(iconPelicula);
                juego.setIcon(iconoVJ);

                JLabel peli = new JLabel("Películas");
                peli.setForeground(new Color(12,6,125));
                peli.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel mus = new JLabel("Canciones");
                mus.setForeground(new Color(12,6,125));
                mus.setFont(new Font("Calibri Light",Font.PLAIN,16));

                JLabel jug = new JLabel("Videojuegos");
                jug.setForeground(new Color(12,6,125));
                jug.setFont(new Font("Calibri Light",Font.PLAIN,16));

                panelfr1.add(cancion);
                panelfr1.add(mus);
                panelfr1.add(todos);
                panelfr2.add(pelicula);
                panelfr2.add(peli);
                panelfr3.add(juego);
                panelfr3.add(jug);

                panelprinc2.add(panelfr2);
                panelprinc2.add(panelfr1);
                panelprinc2.add(panelfr3);

                Frame4.setVisible(true);
                Frame4.setLocationRelativeTo(frame);

                pelicula.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Peliculas");                        
                        frame.setLocation(175, 250);

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return String.class;
                                    case 4:
                                        return String.class;
                                    case 5:
                                        return Double.class;
                                    case 6:
                                        return String.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duracion (min)");
                        modelo.addColumn("Clasificación");
                        modelo.addColumn("Estudio");
                        modelo.addColumn("Precio/artículo ($)");
                        modelo.addColumn("Disponible");

                        for (int i = 0; i < Peliculas.size(); i++) {
                            Object[] fila = new Object[7];
                            fila[0] = Peliculas.get(i).getNombre();
                            fila[1] = Peliculas.get(i).getCantidad();
                            fila[2] = Peliculas.get(i).getDuracion();
                            fila[3] = Peliculas.get(i).getClasificacion();
                            fila[4] = Peliculas.get(i).getEstudio();
                            fila[5] = Peliculas.get(i).getPrecio();
                            if(Peliculas.get(i).getCantidad()>0){
                                fila[6] = "Disponible";
                            }else{
                                fila[6] = "Agotado";
                            }
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                       
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                });

                cancion.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Canciones");  
                        frame.setLocation(175, 250);                      

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return String.class;
                                    case 4:
                                        return String.class;
                                    case 5:
                                        return Integer.class;
                                    case 6:
                                        return Double.class;
                                    case 7:
                                        return String.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duración (seg)");
                        modelo.addColumn("Álbum");
                        modelo.addColumn("Artista");
                        modelo.addColumn("Oyentes");
                        modelo.addColumn("Precio/artículo ($)");
                        modelo.addColumn("Disponible");

                        for (int i = 0; i < Canciones.size(); i++) {
                            Object[] fila = new Object[8];
                            fila[0] = Canciones.get(i).getNombre();
                            fila[1] = Canciones.get(i).getCantidad();
                            fila[2] = Canciones.get(i).getDuracion();
                            fila[3] = Canciones.get(i).getAlbum();
                            fila[4] = Canciones.get(i).getArtista();
                            fila[5] = Canciones.get(i).getOyentes();
                            fila[6] = Canciones.get(i).getPrecio();
                            if(Canciones.get(i).getCantidad()>0){
                                fila[7] = "Disponible";
                            }else{
                                fila[7] = "Agotado";
                            }
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                       
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                }); 
                
                juego.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JFrame frame = new JFrame("Videojuegos");  
                        frame.setLocation(175, 250);                      

                        DefaultTableModel modelo = new DefaultTableModel() {
                            @Override
                            public Class getColumnClass(int column) {
                                switch (column) {
                                    case 0:
                                        return String.class;
                                    case 1:
                                        return Integer.class;
                                    case 2:
                                        return Integer.class;
                                    case 3:
                                        return Integer.class;
                                    case 4:
                                        return String.class;
                                    case 5:
                                        return Double.class;
                                    case 6:
                                        return String.class;
                                    default:
                                        return Boolean.class;
                                }
                            }
                        };

                        modelo.addColumn("Nombre");
                        modelo.addColumn("Cantidad Stock");
                        modelo.addColumn("Duración (min)");
                        modelo.addColumn("Cantidad jugadores");
                        modelo.addColumn("Plataforma");
                        modelo.addColumn("Precio/artículo ($)");
                        modelo.addColumn("Disponible");

                        for (int i = 0; i < Videojuegos.size(); i++) {
                            Object[] fila = new Object[7];
                            fila[0] = Videojuegos.get(i).getNombre();
                            fila[1] = Videojuegos.get(i).getCantidad();
                            fila[2] = Videojuegos.get(i).getDuracion();
                            fila[3] = Videojuegos.get(i).getJugadores();
                            fila[4] = Videojuegos.get(i).getPlataforma();
                            fila[5] = Videojuegos.get(i).getPrecio();
                            if(Videojuegos.get(i).getCantidad()>0){
                                fila[6] = "Disponible";
                            }else{
                                fila[6] = "Agotado";
                            }
                            modelo.addRow(fila);
                        }

                        JTable tabla = new JTable(modelo);

                        JScrollPane scrollPane = new JScrollPane(tabla);
                        scrollPane.setViewportView(tabla);

                        frame.add(scrollPane, BorderLayout.CENTER);                       
                        
                        frame.setSize(1000, 300);
                        frame.setVisible(true);
                    }
                });

                todos.addActionListener(new ActionListener() {
                   public void actionPerformed(ActionEvent e){
                    JFrame frame = new JFrame("Todos los Medios");

                    DefaultTableModel modelo = new DefaultTableModel() {
                        @Override
                        public Class getColumnClass(int column) {
                            switch (column) {
                                case 0:
                                    return String.class;
                                case 1:
                                    return Integer.class;
                                case 2:
                                    return Integer.class; 
                                case 3:
                                    return String.class; 
                                case 4:
                                    return String.class;
                                case 5:
                                    return Integer.class;
                                case 6:
                                    return Double.class; 
                                case 7:
                                    return String.class; 
                                case 8:
                                    return String.class; 
                                default:
                                    return Object.class;
                            }
                        }
                    };

                    modelo.addColumn("Nombre");
                    modelo.addColumn("Cantidad Stock");
                    modelo.addColumn("Duración (s/min/hrs)");
                    modelo.addColumn("Precio/artículo ($)");
                    modelo.addColumn("Disponible");
                    modelo.addColumn("Elemento");

                    for (int i = 0; i<Videojuegos.size();i++) {
                        Object[] fila = new Object[6];
                        fila[0] = Videojuegos.get(i).getNombre();
                        fila[1] = Videojuegos.get(i).getCantidad();
                        fila[2] = Videojuegos.get(i).getDuracion();
                        fila[3] = Videojuegos.get(i).getPrecio();
                        if(Videojuegos.get(i).getCantidad()>0){
                            fila[4] = "Disponible";
                        }else{
                            fila[4] = "Agotado";
                        }
                        fila[5] = "Videojuego";
                        modelo.addRow(fila);
                    }

                    for (int i = 0; i<Peliculas.size();i++) {
                        Object[] fila = new Object[6];
                        fila[0] = Peliculas.get(i).getNombre();
                        fila[1] = Peliculas.get(i).getCantidad();
                        fila[2] = Peliculas.get(i).getDuracion();
                        fila[3] = Peliculas.get(i).getPrecio();
                        if(Peliculas.get(i).getCantidad()>0){
                            fila[4] = "Disponible";
                        }else{
                            fila[4] = "Agotado";
                        }
                        fila[5] = "Pelicula";
                        modelo.addRow(fila);
                    }

                    for (int i = 0;i<Canciones.size();i++) {
                        Object[] fila = new Object[6];
                        fila[0] = Canciones.get(i).getNombre();
                        fila[1] = Canciones.get(i).getCantidad();
                        fila[2] = Canciones.get(i).getDuracion();
                        fila[3] = Canciones.get(i).getPrecio();
                        if(Canciones.get(i).getCantidad()>0){
                            fila[4] = "Disponible";
                        }else{
                            fila[4] = "Agotado";
                        }
                        fila[5] = "Cancion";
                        modelo.addRow(fila);
                    }

                    JTable tabla = new JTable(modelo);

                    JScrollPane scrollPane = new JScrollPane(tabla);
                    JButton txt = new JButton("Generar txt");
                    scrollPane.setViewportView(tabla);

                    frame.add(scrollPane, BorderLayout.CENTER);
                    frame.add(txt, BorderLayout.SOUTH);

                    txt.addActionListener(new ActionListener() {
                        public void actionPerformed(ActionEvent e){
                            try {
                                String lineas = "";
                                String lineas2 = "";
                                String lineas3 = "";
                                BufferedWriter writer = new BufferedWriter(new FileWriter("Inventario.txt"));
                                String infoP = "";
                                String infoC = "";
                                String infoV = "";
                                for(int i=0;i<Peliculas.size();i++){
                                    infoP += "Nombre: " + Peliculas.get(i).getNombre() + ", Cantidad: " + Peliculas.get(i).getCantidad() + ", Duración (mins): " + Peliculas.get(i).getDuracion() + ", Estudio: " + Peliculas.get(i).getEstudio() + ", Clasificación: " + Peliculas.get(i).getClasificacion() + "\n";
                                }
                                for(int i=0;i<Canciones.size();i++){
                                    infoC += "Nombre: " + Canciones.get(i).getNombre() + ", Cantidad: " + Canciones.get(i).getCantidad() + ", Artista: " + Canciones.get(i).getArtista() + ", Duración (s): " + Canciones.get(i).getDuracion() + ", Oyentes mensuales: " + Canciones.get(i).getOyentes() + "\n";
                                }
                                for(int i=0;i<Videojuegos.size();i++){
                                    infoV += "Nombre: " + Videojuegos.get(i).getNombre() + ", Cantidad: " + Videojuegos.get(i).getCantidad() + ", Duración (hrs): " + Videojuegos.get(i).getDuracion() + ", Jugadores: " + Videojuegos.get(i).getJugadores() + ", Plataforma: " + Videojuegos.get(i).getPlataforma() + "\n";
                                }
                                lineas += infoP;
                                lineas2 += infoC;
                                lineas3 += infoV;
                                writer.write("Inventario\n");
                                writer.write("Películas\n");
                                writer.write(lineas);
                                writer.write("Canciones\n");
                                writer.write(lineas2);
                                writer.write("Videojuegos\n");
                                writer.write(lineas3);
                                writer.close();
                                JOptionPane.showMessageDialog(frame, "Ya se generó el archivo txt :)", "Inventario", 1); 
                            } catch (Exception a) {
                                JOptionPane.showMessageDialog(frame, "No se pudo generar el archivo txt :(", "Error", 0); 
                                System.err.println("Error: "+a);
                            }
                        }
                    });

                    frame.setSize(1000, 300);
                    frame.setLocation(175, 250);
                    frame.setVisible(true);
                   } 
                });

            }
        });
        
        db1.attachShutDownHook(Canciones, Peliculas, Videojuegos);

        frame.setVisible(true);
    }
}
