class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Trova il punto del rettangolo più vicino al centro del cerchio
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calcola la distanza tra il centro e il punto più vicino
        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y
        
        # Calcola la distanza al quadrato per evitare radici quadrate (più veloce e senza errori di approssimazione)
        distance_squared = dist_x**2 + dist_y**2
        
        return distance_squared <= radius**2