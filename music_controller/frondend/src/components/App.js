import React from "react";
import { render } from "react-dom";

export default class App extends React.Component {
constructor(props) {
    super(props);

    this.state = {
    };
}

    render() {
        return <div> <h1>Testing React Django</h1> </div>;
    }
}

const AppDiv = document.getElementById('app');
render(<App/>, AppDiv)