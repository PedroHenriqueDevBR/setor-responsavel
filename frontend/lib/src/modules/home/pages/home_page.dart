import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  TabBar _tabBar(ColorScheme appTheme) => TabBar(
        isScrollable: true,
        enableFeedback: true,
        indicatorColor: appTheme.onPrimary,
        labelColor: appTheme.onPrimary,
        unselectedLabelColor: appTheme.onSecondary.withAlpha(100),
        tabs: const [
          Tab(icon: Text('Unidades')),
          Tab(icon: Text('Pontuações')),
          Tab(icon: Text('Penalidades')),
          Tab(icon: Text('Ranking')),
        ],
      );

  @override
  Widget build(BuildContext context) {
    final appTheme = Theme.of(context).colorScheme;
    return DefaultTabController(
      length: 4,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Setor Responsável'),
          bottom: PreferredSize(
            preferredSize: _tabBar(appTheme).preferredSize,
            child: Material(
              color: appTheme.secondary,
              child: Row(
                children: [
                  Expanded(
                    child: Center(child: _tabBar(appTheme)),
                  ),
                ],
              ),
            ),
          ),
        ),
        body: const TabBarView(
          dragStartBehavior: DragStartBehavior.down,
          children: [
            Icon(Icons.directions_car),
            Icon(Icons.directions_transit),
            Icon(Icons.directions_bike),
            Icon(Icons.directions_bike),
          ],
        ),
      ),
    );
  }
}
