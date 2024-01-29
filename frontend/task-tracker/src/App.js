import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'

import {Navibar} from "./Components/Navibar";
import {Route, BrowserRouter as Router, Routes} from "react-router-dom";

import Home from './Home'
import Users from './Users'
import About from './About'
import NotesPage from "./Notes";

function App() {
  return (
      <>
          <Router>
          <Navibar />
          <Routes>
              <Route exact path="/" element={<Home/>} />
              <Route exact path="/users" element={<Users/>} />
              <Route exact path="/notes" element={<NotesPage/>} />
              <Route exact path="/about" element={<About/>} />
          </Routes>
          </Router>
      </>
  );
}

export default App;
