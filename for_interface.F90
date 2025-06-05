
module test
  type :: mytype
    real(8), pointer :: p(:)
  endtype mytype
  type(mytype) :: obj
contains
  subroutine for_alloc(n) bind(C,name="for_alloc")
    use iso_c_binding, only: c_int
    integer(c_int), intent(in), value :: n
    allocate(obj%p(n))
  endsubroutine for_alloc
  subroutine get_ptr(p,n) bind(C,name="get_ptr")
    use iso_c_binding, only: c_ptr, c_loc, c_int
    type(c_ptr)   , intent(out) :: p
    integer(c_int), intent(out) :: n
    p = c_loc(obj%p)
    n = size(obj%p)
  endsubroutine get_ptr
  subroutine print_sum() bind(C,name="print_sum")
    write(*,*) sum(obj%p)
  endsubroutine print_sum
endmodule test

