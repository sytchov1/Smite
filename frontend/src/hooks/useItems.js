import { useMemo } from 'react'

export const useItems = (items, filter) => {
    const searchedItems = useMemo(() => {
        if (filter) {
            return items.filter(item => item.name.toLowerCase().includes(filter.toLocaleLowerCase()));
        }
        return items;
    }, [filter])

    return searchedItems;
}