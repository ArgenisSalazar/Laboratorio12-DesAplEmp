import React, { Component } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import './App.css';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = ({
      prestamos: [],
      pos: null,
      titulo: 'Nuevo',
      id: 0,
      libro: '',
      cliente: '',
      inicio: '',
      fin: '',
    })
    this.cambioId = this.cambioId.bind(this);
    this.cambioLibro = this.cambioLibro.bind(this);
    this.cambioCliente = this.cambioCliente.bind(this);
    this.cambioInicio = this.cambioInicio.bind(this);
    this.cambioFin = this.cambioFin.bind(this);
    this.mostrar = this.mostrar.bind(this);
    this.eliminar = this.eliminar.bind(this);
    this.guardar = this.guardar.bind(this);
  }
  componentDidMount(){
    axios.get('http://localhost:8000/prestamos')
    .then(res =>{
      console.log(res.data);
      this.setState({prestamos: res.data})
    })
  }
  cambioId(e) {
    this.setState( {
      id: e.target.value
    })
  }
  cambioLibro(e) {
    this.setState( {
      libro: e.target.value
    })
  }
  cambioCliente(e) {
    this.setState( {
      cliente: e.target.value
    })
  }
  cambioInicio(e) {
    this.setState( {
      inicio: e.target.value
    })
  }
  cambioFin(e) {
    this.setState( {
      fin: e.target.value
    })
  }
  mostrar(cod,index){
    axios.get('http://localhost:8000/prestamo/'+cod)
    .then(res => {
      this.setState( {
        pos: index,
        titulo: 'Editar',
        id : res.data.idPrestamo,
        libro : res.data.idLibro,
        cliente : res.data.idUsuario,
        inicio : res.data.FecPrestamo,
        fin : res.data.FecDevolucion,
      })
    });
  }
  guardar(e){
    e.preventDefault();
    let cod = this.state.id;
    let datos = {
      idPrestamo : this.state.id,
      idLibro: this.state.libro,
      idUsuario : this.state.cliente,
      FecPrestamo : this.state.inicio,
      FecDevolucion : this.state.fin,
    }
    if(cod>0){
      axios.put('http://localhost:8000/prestamo/'+cod,datos)
      .then(res => {
        let indx = this.state.pos;
        this.state.prestamos[indx] = res.data;
        var temp = this.state.prestamos;
        this.setState( {
          pos: null,
          titulo: 'Nuevo',
          id: 0,
          libro: '',
          cliente: '',
          inicio: '',
          fin: '',
          prestamos : temp
        });
      }).catch((error)=>{
        console.log(error.toString());
      });
    }else{
      axios.post('http://localhost:8000/prestamos', datos)
      .then(res => {
        this.state.prestamos.push(res.data);
        var temp = this.state.prestamos;
        this.setState( {
          id: 0,
          libro: '',
          cliente: '',
          inicio: '',
          fin: '',
          series : temp
        });
      }).catch((error)=>{
        console.log(error.toString());
      });
    }
  }
  eliminar(cod){
    let rpta = window.confirm("Desea eliminar?");
    if(rpta){
      axios.delete('http://localhost:8000/prestamo/'+cod)
      .then(res => {
        var temp = this.state.prestamos.filter((prestamo)=>prestamo.idPrestamo !== cod);
        this.setState({
          prestamos: temp
        })
      });
    }
  }
  render() {
    return(
      
      <div className='div1'>
          <Container>
                <Table striped bordered hover variant="dark">
                <thead class='text-center'>
                  <tr>
                    <th>Ejemplar</th>
                    <th>Libro</th>
                    <th>Cliente</th>
                    <th>Fecha de inicio</th>
                    <th>Fecha de fin</th>
                    <th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {this.state.prestamos.map( (prestamo,index) =>{
                    return (
                      <tr key={prestamo.idPrestamo}>
                        <td>{prestamo.idPrestamo}</td>
                        <td>{prestamo.idLibro}</td>
                        <td>{prestamo.idUsuario}</td>
                        <td>{prestamo.FecPrestamo}</td>
                        <td>{prestamo.FecDevolucion}</td>
                        <td>
                        <Button className='boton' variant="success" onClick={()=>this.mostrar(prestamo.idPrestamo,index)}>Editar</Button>
                        <Button className='boton' variant="danger" onClick={()=>this.eliminar(prestamo.idPrestamo)}>Eliminar</Button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </Table>
              <hr />
              <h1>{this.state.titulo}</h1>
              <Form onSubmit={this.guardar}>
                <Form.Control type="hidden" value={this.state.id} />
                <Form.Group className="mb-3">
                  <Form.Label>Ingrese Ejemplar:</Form.Label>
                  <Form.Control type="text" value={this.state.id} onChange={this.cambioId} />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label>Ingrese Libro:</Form.Label>
                  <Form.Control type="text" value={this.state.libro} onChange={this.cambioLibro} />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label>Ingrese Cliente:</Form.Label>
                  <Form.Control type="text" value={this.state.cliente} onChange={this.cambioCliente} />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label>Ingrese Fecha de Inicio:</Form.Label>
                  <Form.Control type="date" value={this.state.inicio} onChange={this.cambioInicio} />
                </Form.Group>
                <Form.Group className="mb-3">
                  <Form.Label>Ingrese Fecha de Fin:</Form.Label>
                  <Form.Control type="date" value={this.state.fin} onChange={this.cambioFin} />
                </Form.Group>
                <Button className='boton' variant="primary" type="submit">
                  GUARDAR
                </Button>
            </Form>
          </Container>
      </div>
    )
  }
}


export default App;
