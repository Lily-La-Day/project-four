import React from 'react'
import axios from 'axios'
import WritingsIndex from './WritingsIndex'




class SearchIndex extends React.Component {
  constructor() {
    super()
    this.state = {
      query: '',
      category: null,
      filteredWritings: null

    }
    this.handleInputChange = this.handleInputChange.bind(this)
  }

  getInfo () {
    console.log(this.state.category)
    axios.get(`/api/categories/${this.state.category}`)
      .then((res) => {
        this.setState({
          filteredWritings: res.data.writings
        })
      })

  }

  setCategory(data) {
    switch(data) {
      case 'romantic':
        this.setState({
          category: 1
        })
        break
      case 'personal':
        this.setState({
          category: 2
        })
        break
      case 'business':
        this.setState({
          category: 3
        })
        break
      case 'formal':
        this.setState({
          category: 4
        })
        break
      case 'letters of complaint':
        this.setState({
          category: 5
        })
        break
      case 'work':
        this.setState({
          category: 6
        })
        break
      case 'cover letter':
        this.setState({
          category: 7
        })
        break
      case 'cv':
        this.setState({
          category: 8
        })
        break
      case 'family':
        this.setState({
          category: 9
        })
        break
      case 'thank you':
        this.setState({
          category: 10
        })
        break
      case 'application':
        this.setState({
          category: 11
        })
        break
      case 'feedback':
        this.setState({
          category: 12
        })
        break
      case 'prose':
        this.setState({
          category: 13
        })
        break
      case 'short story':
        this.setState({
          category: 14
        })
        break
      case 'obituary':
        this.setState({
          category: 15
        })
        break
      case 'journalism':
        this.setState({
          category: 16
        })
        break
      case 'poetry':
        this.setState({
          category: 17
        })
        break
      case 'formal communication':
        this.setState({
          category: 18
        })
        break
      case 'enquiry':
        this.setState({
          category: 19
        })
        break
      case 'suggestion':
        this.setState({
          category: 20
        })
        break
      case 'criticism':
        this.setState({
          category: 21
        })
        break
      case 'blog':
        this.setState({
          category: 22
        })
        break
      case 'fan fiction':
        this.setState({
          category: 23
        })
        break
      case 'appreciation':
        this.setState({
          category: 24
        })
        break
      case 'branding':
        this.setState({
          category: 25
        })
        break
      case 'press release':
        this.setState({
          category: 26
        })
        break
      default:
        this.setState({
          category: ''
        })


    }
    this.getInfo()


  }

  handleInputChange(e) {
    e.preventDefault()
    console.log(this.state.query, this.state.category)
    this.setState({
      query: this.search.value
    }, () => {
      if (this.state.query && this.state.query.length > 1) {
        this.setCategory(this.state.query)

      }
    })


  }

  render() {
    if(this.state.category) {
      this.getInfo()
    }
    return (
      <main>
        <form>
          <input
            placeholder="Search writing categories..."
            ref={input => this.search = input}
            onChange={this.handleInputChange}
          />
          <p>{this.state.query}</p>
        </form>
        <WritingsIndex filteredWritings={this.state.filteredWritings} category={this.state.category} />
      </main>
    )
  }
}

export default SearchIndex
