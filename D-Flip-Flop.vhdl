library ieee;
use ieee.std_logic_1164.all;

entity d_flipflop is
port( clk, d : in std_logic;
		q 		 : out std_logic);
end d_flipflop;

architecture arc of d_flipflop is
begin 

	q <= d when rising_edge(clk);
	
end arc; 

-- or you can use this 

entity d_flipflop is
port( clk, d : in std_logic;
		q 		 : out std_logic);
end d_flipflop;
architecture arc of d_flipflop is
begin 
	
	process(clk)
	begin 
		if rising_edge(clk) then 
			q <= d;
		end if;
	end process;

end arc;
