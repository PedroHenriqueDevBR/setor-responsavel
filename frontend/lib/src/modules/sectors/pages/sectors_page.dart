import 'package:flutter/material.dart';
import 'package:frontend/src/modules/sectors/widgets/sector_list_widget.dart';
import 'package:frontend/src/modules/sectors/widgets/unity_list_widget.dart';

class SectorsPage extends StatelessWidget {
  const SectorsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const SingleChildScrollView(
      child: Column(
        children: [
          Text('Unidades'),
          SizedBox(height: 8),
          UnityListWidget(),
          SizedBox(height: 16),
          Text('Setores'),
          SizedBox(height: 8),
          SectorsListWidget(),
        ],
      ),
    );
  }
}
