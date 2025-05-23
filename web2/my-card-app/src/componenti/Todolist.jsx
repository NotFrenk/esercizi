import React, {useState} from 'react';

function Todolist() {
   const [todos, setTodos] = useState([]);

   const addTodo = (todo) => {
      setTodos(prevTodos => [...prevTodos, todo]); //aggiungi un nuovo todo
   };

   return (
      <div>
         <button onClick={() => addTodo('Nuovo Todo')}>Aggiungi todo</button>
         <ul>
            {todos.map((todo, index) => (
               <li key={index}>{todo}</li>
            ))}
         </ul>
      </div>
   );
}; 
export default Todolist