import React, {useState} from 'react'
import Slot from './Slot'
import Modal from './UI/modal/Modal'
import ItemPicker from './ItemPicker'

function Equipment({eqip, setEqip}) {
  const [modal, setModal] = useState(false);
  const [slot, setSlot] = useState({slot: null, item: null});

  const pickItem = (slot, item) => {
    console.log(item);
    let newEqip = [...eqip];
    const index = newEqip.findIndex(e => e.slot === slot);
    newEqip[index].value = item;
    setEqip([...newEqip]);
  }

  return (
    <div className='Equipment'>
        <div className='equip-column'>
          {eqip.slice(0, 10).map((e, index) =>
            <Slot key={index} name={e.slot} item={e.value}
              openModal={
                (slot, item) => {
                  setSlot({slot: slot, item: item});
                  setModal(true);
                }
              }
            />
          )}
        </div>
        <div className='equip-column'>
          {eqip.slice(10, 19).map((e, index) =>
            <Slot key={index} name={e.slot} reverse={'row-reverse'} item={e.value} 
              openModal={(slot, item) => {
                setSlot({slot: slot, item: item});
                setModal(true);
                }
              }
            />
          )}
        </div>
        <Modal visible={modal} setVisible={setModal}>
          <ItemPicker slot={slot} pickItem={pickItem} setModal={setModal}/>
        </Modal>
    </div>
    
  )
}

export default Equipment