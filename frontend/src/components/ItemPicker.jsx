import React, { useState, useEffect } from 'react'
import ItemSearch from './ItemSearch'
import ItemList from './ItemList'
import { Service } from '../API/Service';
import Loader from './UI/loader/Loader';
import Button from './UI/button/Button';
import { useFetching } from '../hooks/useFetching';
import { useItems } from '../hooks/useItems';

function ItemPicker(props) {
  const [items, setItems] = useState([]);
  const [filter, setFilter] = useState('');
  const [fetchItems, isLoading, itemsError] = useFetching(async () => {
    const response = await Service.getItems();
    setItems([...response.data])
  })
  const filteredItems =  useItems(items, filter);
  const [chosenItem, setChosenItem] = useState(props.slot['item']);
  
  
  useEffect(() => {
    fetchItems();
  }, [])

  useEffect(() => {
    setChosenItem(props.slot['item']);
  }, [props.slot])

  const choseItem = (item) => {
    setChosenItem(item);
    props.pickItem(props.slot['slot'], item);
    props.setModal(false);
  }

  const resetItem = () => {
    setChosenItem(null);
    props.pickItem(props.slot['slot'], null);
  }

  return (
    <div className='ItemPicker'>
        <div className='ItemPicker-header'>
            <ItemSearch filter={filter} setFilter={setFilter}/>
            <div className='ItemPicker-slot'>{props.slot['slot']}</div>
        </div>
        {itemsError &&
          <h1>Произошла ошибка {itemsError}</h1>
        }
        <ItemList items={filteredItems} chosenItem={chosenItem} setChosenItem={setChosenItem} choseItem={choseItem}/>
        {isLoading &&
          <div style={{display: 'flex', justifyContent: 'center', marginTop: '50px'}}>
            <Loader></Loader>
          </div>
        }
        {chosenItem &&
          <Button className='resetItemBtn' onClick={resetItem}>Сбросить</Button>
        }
    </div>
  )
}

export default ItemPicker