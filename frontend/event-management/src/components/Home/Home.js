import React from "react";
import { Link } from "react-router-dom";

function Home(props) {
  return (
    <div>
      <div>
        <h1>
          <Link to="/login">Login</Link>
        </h1>
        <br />
        <h1>
          <Link to="/signup">Signup</Link>
        </h1>
      </div>

      <br />
      <br />
      <br />

      <h3> {props.name ? `Welcome - ${props.name}` : "Login please"}</h3>
    </div>
  );
}

export default Home;
