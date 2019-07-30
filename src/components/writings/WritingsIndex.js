import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import HorizontalScroll from 'react-scroll-horizontal'



class WritingsIndex extends React.Component {
  constructor() {
    super()

    this.state = { writings: null,  num: 0 }
    this.addOne = this.addOne.bind(this)
    this.minusOne = this.minusOne.bind(this)


  }

  componentDidMount() {
    axios.get('/api/writings')
      .then(res => this.setState({ writings: res.data }))
      .catch(err => console.log(err))
  }

  addOne() {
    let number = this.state.num
    number += 1
    this.setState({ num: number })
  }

  minusOne() {
    let number = this.state.num
    number -= 1
    this.setState({ num: number })
  }




  render() {
console.log(this.props.filteredWritings)
    if (!this.state.writings) return null


    return (

      <main className="index-main">


        {!this.props.filteredWritings && <div>


          <div className="writings-container scroll" >
            {this.state.writings.map((writing, i) => (
              <Link key={i} to={`/edit-writings/${writing.id}`}>
                <h3 key={writing.id} > {writing.title}</h3>
              </Link>


            ))}

          </div>

          {this.state.writings.map((writing, i) => (

            <div key={i} >
              {(this.state.num === i) &&
              <Link to={`/edit-writings/${writing.id}`}>

                <h3 className="writing-title" key={i}>
                  {writing.title}</h3>
                <p className="index-writing-show" >
                  {writing.text}


                </p>

              </Link>}

            </div>

          ))}
      {this.state.num > 0 &&  <button onClick={this.minusOne}  className="show-writing-button">Last Writing</button>}
    {this.state.num < this.state.writings.length &&      <button onClick={this.addOne} className="show-writing-button">Next Writing</button>}



        </div> }

        {this.props.filteredWritings && <div>
          <div className="writings-container scroll">
            {this.props.filteredWritings.map((writing, i) => (
              <Link to={`/edit-writings/${writing.id}`}>
                <h3 key={writing.id}> {writing.title}</h3>
              </Link>


            ))}
          </div>
          {this.props.filteredWritings.map((writing, i) => (

            <div key={i} className ="shown-writing">
              {(this.state.num === i) &&
              <Link to={`/edit-writings/${writing.id}`}>

              <h3 className="writing-title" key={i}>
                {writing.title}</h3>
              <p className="index-writing-show" > {writing.text}</p>
              <button className="show-writing-button">See More</button>
              </Link>}

            </div>


          ))}

  {this.state.num > 0 &&   <button onClick={this.minusOne}  className="show-writing-button">Last Writing</button>}
  {this.state.num < this.props.filteredWritings.length && <button onClick={this.addOne} className="show-writing-button">Next Writing</button>}
        </div> }



      </main>
    )
  }
}

export default WritingsIndex
