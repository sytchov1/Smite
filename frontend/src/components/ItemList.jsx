import React from 'react'
import Item from './Item'

function ItemList(props) {
  return (
    <div className='ItemList'>
      {props.items.length
        ? props.items.map((item, index) =>
          <Item key={index} item={item} setChosenItem={props.setChosenItem} chosenItem={props.chosenItem} choseItem={props.choseItem}></Item>)
        : <div style={{width: '100%', textAlign: 'center'}}>Ничего не найдено :(</div>}
    </div>
  )
}

export default ItemList