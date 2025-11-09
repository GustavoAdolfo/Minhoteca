export type FilterDTO = {
  filterTerm?: string;
  filterValue?: string;
  sortTerm?: string;
  sortValue: string;
  localFirst: boolean;
  pageLimit: number;
  skip: number;
};

export const defaultFilter: FilterDTO = {
  filterTerm: '',
  filterValue: '',
  sortTerm: '',
  sortValue: 'ASC',
  localFirst: true,
  pageLimit: 10,
  skip: 0,
};
