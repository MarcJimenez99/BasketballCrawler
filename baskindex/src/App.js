import React from 'react';
import './App.css';
import axios from 'axios';


export default class App extends React.Component {
state = {
  srch: '',
  dataList:[[]]
};

  //curl -X GET -u $username:$password "$endpoint/$indexname/_search?pretty" -H "Content-Type: application/json" -d"{\"query\": {\"match\": {\"html\": \"Harden\"}}}"
searchfunc = event => {
  event.preventDefault();
  const query = {
    srch: this.state.srch
  }
  console.log(query)
  axios.post(`http://localhost:5000/performQuery`, {query})
  .then(res => {
    console.log(res.data);
    this.setState({dataList: res.data})
  })
}

handleChange = (evt) => {
  evt.preventDefault();
  this.setState({[evt.target.name]: evt.target.value});
}

printTable() {
  let array = []
  if (this.state.dataList.length > 1) {
    for (let k in this.state.dataList) {
      array.push(<tr>
        <th><b>{this.state.dataList[k][0]}</b></th>
        <th><a href = {this.state.dataList[k][1]}>{this.state.dataList[k][1]}</a></th>
        <th>{this.state.dataList[k][2]}</th>
      </tr>
        )
    }
  }
  return array;
}



render() {
  return (
    <div className="App">
      <h1>Enter search query</h1>
      <form onSubmit = {this.searchfunc}>
        <div><input type = "text" placeholder= "Enter query here" name = "srch" onChange = {this.handleChange}/> </div>
        <button type = "submit"> Submit </button>
      </form>
          <table>
            <tr>
              <th>Score</th>
              <th>URL</th>
              <th>Crawled Page #</th>
            </tr>
            {this.printTable()}
          </table>
    </div>
  );
}

}