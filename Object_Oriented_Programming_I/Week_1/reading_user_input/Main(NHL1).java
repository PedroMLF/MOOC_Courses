
import nhlstats.NHLStatistics;

public class Main {

    public static void main(String[] args) {
        // Top 10 players based on goals
        NHLStatistics.sortByGoals();
        NHLStatistics.top(10);
        // Top 25 players on penalty amoutns
        NHLStatistics.sortByPenalties();
        NHLStatistics.top(25);
        // Print stats for Sidney Crosby
        NHLStatistics.searchByPlayer("Sidney Crosby");
        // Print stats for the Philadelphia Flyers
        NHLStatistics.teamStatistics("PHI");
        // Prints players in Anaheim Ducks ordered by points
        NHLStatistics.sortByPoints();
        NHLStatistics.teamStatistics("ANA");
    }
}
