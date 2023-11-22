import 'package:flutter/material.dart';
import 'package:frontend/src/shared/theme/app_images.dart';

class PresentationPage extends StatelessWidget {
  const PresentationPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Center(
        child: Image.asset(AppImages.leafs, width: 250),
      ),
    );
  }
}
