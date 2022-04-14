import React from 'react'
import Input from './UI/input/Input'

function ItemSearch({filter, setFilter}) {
  return (
    <div className='ItemSearch'>
      <Input
        value={filter}
        onChange={e => setFilter(e.target.value)}
        placeholder='Поиск...'
      />
    </div>
  )
}

export default ItemSearch