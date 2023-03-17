library ieee;
use ieee.std_logic_1164.all;

entity d_flipflop is
port( clk, d : in std_logic;
		q 		 : out std_logic);
end d_flipflopl

architecture arc of d_flipflop is
begin 
	q <= d when rising_edge(clk);
end arc; 
