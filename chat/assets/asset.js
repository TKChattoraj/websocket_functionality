import { rangeRight } from "lodash";
import React from "react";
import ReactDOM from "react-dom/client";

function Open_button(props) {
  console.log("In the open button " + props.message);
  function b_click(e) {
    console.log("In the b_click");
    props.on_click(props.message, props.ws, props.context);
  }
  return (
    <button onClick={b_click} disabled={props.disabled}>
      Open Channel
    </button>
  );
}

class OpenChannel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      button: true,
      text: "No Channel",
      disabled: false,
    };
    console.log("First This");
    console.log(this);
    parent = this;
    console.log("First Parent");
    console.log(parent);
    this.ws = new WebSocket("wss://" + window.location.host + "/ws/chat/");

    this.ws.onopen = () => {
      console.log("connected websocket");
    };

    this.ws.onmessage = function (e) {
      console.log("message received");
      const data = JSON.parse(e.data);
      console.log("onmessage");
      console.log(data.message);
      console.log("This:");
      console.log(this);
      console.log("Parent");
      console.log(parent);
      parent.setState({
        text: data.message,
      });
    };
  }

  /***************

const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/chat/'
  + roomName
  + '/'
);

chatSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  document.querySelector('#chat-log').value += (data.message + '\n');
  document.getElementById('channel_state').innerHTML = data.message;
  
};

chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};


*****************/

  button_click(message, ws, context) {
    console.log(message);

    ws.send(JSON.stringify({ message: message + message + message }));
    console.log("button_click");
    console.log(this);
    context.setState({
      disabled: true,

      text: "React Client side state change:  Client telling server to tell LN Node to Open Channel...",
    });
  }

  render() {
    let message;
    message = "Hi Titan!";
    console.log("In the OpenChannel Render");
    console.log(message);

    return (
      <div>
        <Open_button
          button={this.state.button}
          on_click={this.button_click}
          message={"Hello Champ!"}
          ws={this.ws}
          context={parent}
          disabled={this.state.disabled}
        />
        <h1>Channel Status:</h1>
        <h3> {this.state.text}</h3>
      </div>
    );
  }
}

//=======================================================

const asset = ReactDOM.createRoot(document.getElementById("asset"));

asset.render(<OpenChannel />);
