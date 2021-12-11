flash_count = 0

def flash(grid, pos):
    global flash_count
    r, c = pos
    
    if grid[r][c] == 0:
        return
    
    grid[r][c] += 1
    
    if grid[r][c] >= 10:  # Flash
        flash_count += 1
        grid[r][c] = 0
    else:
        return
    
    # Top Left
    if r > 0 and c > 0:
        flash(grid, (r-1, c-1))
    
    # Top
    if r > 0:
        flash(grid, (r-1, c))

    # Top Right
    if r > 0 and c < 9:
        flash(grid, (r-1, c+1))

    # Right
    if c < 9:
        flash(grid, (r, c+1))

    # Bottom Right
    if r < 9 and c < 9:
        flash(grid, (r+1, c+1))
    
    # Bottom 
    if r < 9:
        flash(grid, (r+1, c))

    # Bottom Left
    if r < 9 and c > 0:
        flash(grid, (r+1, c-1))

    # Left
    if c > 0:
        flash(grid, (r, c-1))
