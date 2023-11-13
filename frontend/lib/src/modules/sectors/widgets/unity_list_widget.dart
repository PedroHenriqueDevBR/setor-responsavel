import 'package:flutter/material.dart';
import 'package:frontend/src/modules/sectors/widgets/unity_widget.dart';

class UnityListWidget extends StatelessWidget {
  const UnityListWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: Row(
        children: [
          UnityWidget(),
          UnityWidget(selected: true),
          UnityWidget(),
          UnityWidget(),
          UnityWidget(),
        ],
      ),
    );
  }
}
