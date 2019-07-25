import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './style.scss'
import WritingsIndex from './components/writings/writingsIndex'
import EditCreate from './components/writings/EditCreate'
import EditorLogin from './components/Auth/EditorLogin'





const App = () => {
  return (
    <BrowserRouter>
      <main>
        <div>
          <Switch>
            <Route path='/editorlogin' component={EditorLogin} />
            <Route path='/writings/:id' component={EditCreate} />
            <WritingsIndex />
          </Switch>
        </div>
      </main>
    </BrowserRouter>

  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
